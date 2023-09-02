from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from product.models import Product
from product.myserializer import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
=======
>>>>>>> 0b90fc02c936df97fc0742e622f2b66581bcb74a
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
