from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, MyUserView, LocationView, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r"location", LocationView)
router.register(r'users', MyUserView)
router.register(r'carts', CartViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/accounts/', include('authemail.urls'))
]
