from celery import shared_task
from .models import Order


@shared_task
def change_order_status(order_id, new_status):
    try:
        order = Order.objects.get(pk=order_id)
        order.status = new_status
        order.save()
        return f"Order status updated to {new_status} for order {order_id}"
    except Order.DoesNotExist:
        return f"Order with ID {order_id} does not exist."
