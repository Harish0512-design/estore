from django.contrib.auth.models import User
from rest_framework import serializers

from product.models import Product, Review, Location, Cart, Order, OrderHistory, UserType


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class LocationSerializer(serializers.HyperlinkedModelSerializer):
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


class OrderTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserType
        fields = "__all__"
