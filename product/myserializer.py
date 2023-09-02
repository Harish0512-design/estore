from django.contrib.auth.models import User
from rest_framework import serializers

from product.models import *


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(view_name='MyUserView', queryset=MyUser.objects.all(),
    #                                            lookup_field='pk')

    class Meta:
        model = Location
        fields = "__all__"


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory
        fields = "__all__"


class UserTypeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='myuser-detail',
        queryset=MyUser.objects.all())

    class Meta:
        model = UserType
        fields = "__all__"


class BuyerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyerProfile
        fields = "__all__"


class SellerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"
