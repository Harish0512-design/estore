
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from product.models import Product
from product.myserializer import ProductSerializer, MyUserSerializer, LocationSerializer, UserTypeSerializer, BuyerProfileSerializer, SellerProfileSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class MyUserView(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserTypeView(ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class BuyerProfileAPIView(APIView):
    def get(self, request):
        buyer_profile = BuyerProfile.objects.all()
        serializer = BuyerProfileSerializer(buyer_profile, many=True)
        return Response(serializer.data)

    # def post(self,request):

    def put(self, request):
        serializer = BuyerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            buyer_profile = BuyerProfile.objects.get(pk=request.data['id'])
            serializer.update(buyer_profile, serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerProfileViewset(ModelViewSet):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer

    def perform_create(self, serializer):
        usertype = UserType.objects.get(user=self.request.user)
        if usertype.type == 'Seller':
            serializer.save(UserType=usertype)
        else:
            return Response({"detail": "you are a buyer,buyers can't create SellerProfile."},
                            status=status.HTTP_400_BAD_REQUEST)

