from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from product.custom_permissions import IsSeller, IsBuyer
from product.models import Product, MyUser, Location, Cart
from product.myserializer import ProductSerializer, LocationSerializer, CartSerializer, MyUserSerializer
from .order import get_cart_items, get_product_price, calculate_products_price_in_cart, calculate_total_price


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
    permission_classes = [permissions.IsAuthenticated, IsBuyer]
    queryset = Cart.objects.all().order_by('-id')
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


@api_view(['GET', 'POST'])
def order_now_api(request):
    if request.method == 'GET':
        products = calculate_products_price_in_cart(request)
        total_price = calculate_total_price(request)
        user = request.user
        return Response({'products': products, 'total price': total_price, 'order_by': user},
                        status=status.HTTP_200_OK)
    # elif request.method == 'POST':
    #     serializer = DeliveryAddressSerializer(data=request.data)
    #     if serializer.is_valid():
    #         ordered_items = calculate_products_price_in_cart(request)
    #         total_price = calculate_total_price(request)
    #         ordered_by = request.user
    #         delivery_address = serializer.data.get('delivery_address')
