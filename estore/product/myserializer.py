from django.contrib.auth.models import User
from rest_framework import serializers

from product.models import *


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for k, v in validated_data:
            setattr(instance, k, v)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = "__all__"


class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=4, required=True)
    confirm_password = serializers.CharField(min_length=4, required=True)


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
