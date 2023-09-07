from product.models import Cart, Product, Location, MyUser, Order


def get_user_details(request):
    print(request.user)
    user_obj = MyUser.objects.get(id=request.user.id)
    return user_obj


def get_cart_items(request) -> dict:
    cart_items = Cart.objects.filter(user=request.user.id).values()
    return cart_items


def get_delivery_address(request):
    del_loc_obj = Location.objects.filter(user=request.user.id).values()
    return del_loc_obj


def get_product_billing_address(product_id):
    product_obj = Product.objects.get(id=product_id)
    bill_loc_obj = Location.objects.filter(user=product_obj.added_by).values()
    return list(bill_loc_obj)


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
        billing_address = get_product_billing_address(id)
        prod_dict = {"id": id, "quantity": quantity, "price per single unit": prod_price,
                     "price": prod_price * quantity, "billing_address": billing_address}
        price_of_products_in_carts.append(prod_dict)
    return price_of_products_in_carts


def calculate_total_price(request) -> float:
    products = calculate_products_price_in_cart(request)
    total_price = 0
    for product in products:
        total_price += product.get('price')

    return total_price


def insert_order_data_into_db(request):
    id = request.data.get('delivery_address')
    loc_obj = Location.objects.get(id=id)
    data = {
        "ordered_items": calculate_products_price_in_cart(request),
        "total_price": calculate_total_price(request),
        "ordered_by": get_user_details(request),
        "delivery_address": loc_obj
    }
    try:
        order_obj = Order.objects.create(**data)
        print(order_obj)
        if order_obj:
            return 1
        else:
            return -1
    except Exception as e:
        print(e)
