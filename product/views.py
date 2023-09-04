from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from product.custom_permissions import IsSeller, IsBuyer
from product.models import Product, MyUser, Location, Cart
from product.myserializer import ProductSerializer, MyUserSerializer, LocationSerializer, CartSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSeller]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MyUserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class LocationViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CartViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, IsBuyer]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderNow(APIView):
    def get(self, request):
        print(Cart.objects.filter(user = request.user))
        return Response({'response': 'success'}, status=status.HTTP_200_OK)

    def post(self):
        lst = OrderNow(self.request, Cart)
        print(lst)
