from authemail.models import EmailUserManager, EmailAbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL, DO_NOTHING


# Create your models here.
class MyUser(EmailAbstractUser):
    # Required
    objects = EmailUserManager()
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.first_name, self.email)


# class UserType(models.Model):
#     user = models.ForeignKey(to=MyUser, on_delete=CASCADE)
#     type = models.CharField(max_length=8, null=True, blank=False, choices=(('Seller', 'Seller'), ('Buyer', 'Buyer')))
#
#     # def __str__(self):
#     #     return self.user


class Location(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=SET_NULL, null=True, blank=False)
    phone = models.CharField(validators=[RegexValidator("^[6-9]{1}\d{9}$")], max_length=15)
    address = models.TextField()
    landmark = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45)
    pincode = models.IntegerField(validators=[MinValueValidator(000000), MaxValueValidator(999999)])
    state = models.CharField(max_length=45)

    def __str__(self):
        return "%s(%s, %s, %s - %s)" % (self.user, self.address, self.city, self.state, self.state)


# class BuyerProfile(models.Model):
#     userType = models.OneToOneField(to=UserType, on_delete=CASCADE)
#     gender = models.CharField(null=True, blank=True, max_length=6, choices=(('m', 'male'), ('f', 'female')))
#     address = models.ForeignKey(to=Location, on_delete=CASCADE, blank=True, null=True)
#
#
# class SellerProfile(models.Model):
#     userType = models.OneToOneField(to=UserType, on_delete=CASCADE)
#     store = models.CharField(max_length=100, null=True, blank=True)
#     address = models.ForeignKey(to=Location, on_delete=CASCADE, null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=CASCADE)
    rating = models.FloatField(validators=(MaxValueValidator(5), MinValueValidator(1)))
    comments = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.user, self.rating)


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

    def __str__(self):
        return f"{self.name}(price : {self.price}, brand: {self.brand}, in-stock : {self.in_stock})"


class Cart(models.Model):
    user = models.OneToOneField(to=MyUser, on_delete=CASCADE)
    product = models.ForeignKey(to=Product, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s - %s" % (self.product, self.quantity, self.is_purchased)


class Order(models.Model):
    cart = models.OneToOneField(to=Cart, on_delete=DO_NOTHING)
    total_price = models.FloatField()
    billing_address = models.TextField()
    delivery_address = models.TextField()
    ordered_date = models.DateTimeField(auto_now_add=True)


class OrderHistory(models.Model):
    user = models.ForeignKey(to=MyUser, on_delete=DO_NOTHING)
    order = models.OneToOneField(to=Order, on_delete=DO_NOTHING)
