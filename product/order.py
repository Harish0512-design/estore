from product.models import Cart, Product, Location


def get_cart_items(request) -> dict:
    cart_items = Cart.objects.filter(user=request.user).values()
    return cart_items


def get_product_price(pk: int) -> float:
    prod_obj = Product.objects.get(id=pk)
    return prod_obj.price


def calculate_products_price_in_cart(request) -> list:
    cart_items = get_cart_items(request)
    price_of_products_in_carts = []
    for item in cart_items:
        id = item.get('product_id')
        quantity = item.get('quantity')
        prod_price = get_product_price(id)
        prod_dict = {"id": id, "quantity": quantity, "price per single unit": prod_price,
                     "price": prod_price * quantity}
        price_of_products_in_carts.append(prod_dict)
    return price_of_products_in_carts


def calculate_total_price(request) -> float:
    products = calculate_products_price_in_cart(request)
    total_price = 0
    for product in products:
        total_price += product.get('price')

    return total_price


def get_delivery_address(request):
    loc_obj = Location.objects.filter(user=request.user).values()
    return loc_obj
