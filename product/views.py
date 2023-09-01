from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.myserializer import ProductSerializer, UserSerializer, PasswordChangeSerializer
from rest_framework.permissions import IsAuthenticated

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
