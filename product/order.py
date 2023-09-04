from product.models import Cart


class OrderNow:
    def __init__(self, request, model) -> None:
        self.request = request
        self.model = model

    def get_cart_items(self):
        cart_obj = self.model.objects.filter(user=self.request.user)
        for items in cart_obj:
            return items


obj = OrderNow('harishsomsole12@gmail.com',Cart)
print(obj.get_cart_items())