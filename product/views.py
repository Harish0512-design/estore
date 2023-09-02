from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.myserializer import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
