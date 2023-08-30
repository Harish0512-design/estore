from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, UserRegisterView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/accounts/', UserRegisterView.as_view())
]
