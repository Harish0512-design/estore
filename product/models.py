from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, MaxLengthValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL, RESTRICT, DO_NOTHING
from authemail.models import EmailUserManager, EmailAbstractUser


class MyUser(EmailAbstractUser):
    # Required
    objects = EmailUserManager()


# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=CASCADE)
    type = models.CharField(max_length=8, null=True, blank=True, choices=(('Seller', 'Seller'), ('Buyer', 'Buyer')))


class Location(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=SET_NULL, null=True, blank=False)
    phone = models.CharField(validators=[RegexValidator("^0?[6-9]{1}\d{9}$")], max_length=15)
    address = models.TextField()
    landmark = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45)
    pincode = models.IntegerField(validators=[MaxLengthValidator(6), MinValueValidator(6)])
    state = models.CharField(max_length=45)


class BuyerProfile(models.Model):
    userType = models.OneToOneField(to=UserType, on_delete=CASCADE)
    gender = models.CharField(null=True, blank=True, max_length=6, choices=(('m', 'male'), ('f', 'female')))
    address = models.ForeignKey(to=Location, on_delete=CASCADE)


class SellerProfile(models.Model):
    userType = models.OneToOneField(to=UserType, on_delete=CASCADE)
    store = models.CharField(max_length=100, null=True, blank=True)
    address = models.ForeignKey(to=Location, on_delete=CASCADE)


class Review(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=CASCADE)
    rating = models.FloatField(validators=(MaxValueValidator(5), MinValueValidator(1)))
    comments = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=45)
    price = models.FloatField()
    in_stock = models.IntegerField()
    color = models.CharField(max_length=45)
    size = models.CharField(max_length=5)
    image = models.ImageField(upload_to='uploads/%Y/%M/%D')
    rating = models.OneToOneField(to=Review, on_delete=CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(to=MyUser, on_delete=CASCADE)
    product = models.ForeignKey(to=Product, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    is_purchased = models.BooleanField(default=False)


class Order(models.Model):
    cart = models.OneToOneField(to=Cart, on_delete=DO_NOTHING)
    total_price = models.FloatField()
    billing_address = models.TextField()
    delivery_address = models.TextField()
    ordered_date = models.DateTimeField(auto_now_add=True)


class OrderHistory(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=DO_NOTHING)
    order = models.OneToOneField(to=Order, on_delete=DO_NOTHING)
