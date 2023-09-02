from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from product.custom_permissions import IsSeller, IsBuyer
from product.models import Product, MyUser, Location, Cart
from product.myserializer import ProductSerializer, MyUserSerializer, LocationSerializer, CartSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSeller]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MyUserView(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class LocationView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CartViewSet(ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated, IsBuyer]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
