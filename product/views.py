from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from product.models import Product
from product.myserializer import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
