import random

from product.models import Product


def add_in_stock_to_product():
    for i in Product.objects.all():
        i.in_stock = random.randint(0, 100)
        i.save()
    return 0
