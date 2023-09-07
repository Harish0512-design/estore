from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from product.custom_permissions import IsSeller, IsBuyer
from product.models import Product, MyUser, Location, Cart, Order
from product.myserializer import ProductSerializer, LocationSerializer, CartSerializer, MyUserSerializer, \
    OrderSerializer
from .order import insert_order_data_into_db


# Create your views here.
class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsSeller]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MyUserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class LocationViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CartViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsBuyer]
    queryset = Cart.objects.all().order_by('-id')
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


@api_view(['GET', 'POST'])
def order_now(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        result = insert_order_data_into_db(request)
        # print(result)
        if result == 1:
            return Response({'response': 'order placed successfully'}, status=status.HTTP_200_OK)
        return Response({'delivery_address': 'This field is mandatory'}, status=status.HTTP_400_BAD_REQUEST)
