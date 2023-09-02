from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView, PasswordChangeView
from rest_framework.routers import DefaultRouter

from product.views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r"location", LocationView)
router.register(r'myuser', MyUserView)
router.register(r"usertype", UserTypeView)
# router.register(r"buyerprofile", BuyerProfileAPIView, basename='buyerprofile')
router.register(r'sellerprofile', SellerProfileViewset)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/accounts/', include('authemail.urls')),
    path('api/accounts/register/', UserRegisterView.as_view()),
    path('api/accounts/change-password', PasswordChangeView.as_view()),
    path("api/location/", include(router.urls)),
    path("api/myuser/", include(router.urls)),
    path('api/usertype/', include(router.urls)),
    path('api/usertype/buyerprofile/', BuyerProfileAPIView.as_view()),
    path('api/usertype/sellerprofile', include(router.urls))
]
