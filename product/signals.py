from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import UserType, SellerProfile, BuyerProfile


@receiver(post_save, sender=User)
def save_user_type(sender, instance, created, **kwargs):
    if created:
        UserType.objects.create(user=instance)


@receiver(post_save, sender=UserType)
def save_buyer_seller_profiles(sender, instance, created, **kwargs):
    if created:
        if instance.type == "Seller":
            SellerProfile.objects.create(userType=instance)
        elif instance.type == "Buyer":
            BuyerProfile.objects.create(userType=instance)
