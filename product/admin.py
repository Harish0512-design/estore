from django.contrib import admin
from django.contrib.admin import ModelAdmin

from product.models import Product, Location, Review, UserType, Cart, Order, OrderHistory


# Register your models here.
class ProductAdmin(ModelAdmin):
    list_filter = ['created_date', 'brand', 'size']
    list_display = ['name', 'price']
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(Location)
admin.site.register(Review)
admin.site.register(UserType)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderHistory)
