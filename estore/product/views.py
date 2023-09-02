from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from product.myserializer import *


# Create your views here.
class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'user with username ' + request.data['username'] + ' created successfully '},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    def post(self, request):
        user = request.user
        serializer = PasswordChangeSerializer(data=request.data)
        users = User.objects.all()
        if serializer.is_valid():
            new_password = serializer.data.get('new_password')
            confirm_password = serializer.data.get('confirm_password')
            if user in users:
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return Response({'response': 'Password changed successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'response': 'Password and confirm password should be same'},
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'response': user + ' is not a valid user'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserView(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class LocationView(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserTypeView(ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


#
# class BuyerProfileView(generics.GenericAPIView):
#     serializer_class = BuyerProfileSerializer
#     basename = 'buyerprofile'
#
#     def post(self, request):
#         # extracting data from the request
#         user_type_id = request.data.get('user_type')
#         location_id = request.data.get('location')
#
#         try:
#             user_type = UserType.objects.get(id=user_type_id)
#         except ObjectDoesNotExist:
#             return Response({'message': 'UserType does not exist'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             location = Location.objects.get(id=location_id)
#         except ObjectDoesNotExist:
#             return Response({'message': 'Location does not exist'}, status=status.HTTP_400_BAD_REQUEST)
#
#             # create new buyerprofile with provided data
#         buyer_profile = BuyerProfile.objects.create(userType=user_type, address=location,
#                                                     gender=request.data.get('gender'))
#
#         serializer = self.get_serializer(buyer_profile)
#         headers = self.get_success_headers(serializer.data)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#         # except UserType.DoesNotExist:
#     return Response({'message':'UserType does not exist'},status=status.HTTP_400_BAD_REQUEST)
# except Location.DoesNotExist:
#     return Response({'message':'Location does not exist'},status=status.HTTP_400_BAD_REQUEST)

#
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
