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
