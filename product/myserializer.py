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


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = MyUserSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'quantity', 'is_purchased', 'user', 'product']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHistory
        fields = "__all__"
