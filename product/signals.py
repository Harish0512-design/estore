from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Order, Cart, Product
from product.order import get_product_id_and_quantity


@receiver(post_save, sender=Order)
def save_to_db(sender, instance, created, **kwargs):
    if created:
        Cart.objects.filter(user=instance.ordered_by).update(is_purchased=True)
        prod_quantities = get_product_id_and_quantity(instance.ordered_items)
        print(prod_quantities)
        for prod_item in prod_quantities:
            # print(prod_item)
            prod_obj = Product.objects.get(id=prod_item.get('id'))
            in_stock_quantity = prod_item.get('quantity')
            quantity = prod_obj.in_stock
            # print(in_stock_quantity)
            # print(quantity)
            prod_obj.in_stock = (quantity - in_stock_quantity)
            prod_obj.save()
