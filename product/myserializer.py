from django.contrib.auth.models import Group
from rest_framework import serializers

from product.models import Product, MyUser, Location, Cart, Order, OrderHistory, Review


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class MyUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'is_active', 'groups']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ('added_by',)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = MyUserSerializer()

    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'is_purchased', 'user']


class OrderSerializerIn(serializers.Serializer):
    delivery_address = serializers.IntegerField()


class OrderSerializerOut(serializers.ModelSerializer):
    ordered_by = MyUserSerializer()
    delivery_address = LocationSerializer()


class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory
        fields = "__all__"
