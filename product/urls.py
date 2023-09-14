from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, MyUserViewSet, LocationViewSet, CartViewSet, order_now, ReviewViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r"location", LocationViewSet)
router.register(r'users', MyUserViewSet)
router.register(r'carts', CartViewSet)
router.register(r'reviews', ReviewViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/order-now/', order_now),
]
