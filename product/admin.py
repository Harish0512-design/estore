from django.contrib import admin
from django.contrib.admin import ModelAdmin
from product.models import *
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin
from rest_framework.authtoken.models import Token


class MyUserAdmin(EmailUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'is_verified',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom info', {'fields': ('date_of_birth',)}),
    )


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), MyUserAdmin)


# Register your models here.
class ProductAdmin(ModelAdmin):
    list_filter = ['created_date', 'brand', 'size']
    list_display = ['name', 'price']
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(Location)
admin.site.register(Review)
# admin.site.register(UserType)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderHistory)
# admin.site.register(BuyerProfile)
# admin.site.register(SellerProfile)
