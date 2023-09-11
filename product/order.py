from django.db.models import Q
from rest_framework.request import Request

from product.models import Cart, Product, Location, MyUser, Order


def get_user_details(request: Request) -> MyUser:
    # print(request.user.id)
    user_obj = MyUser.objects.get(id=request.user.id)
    return user_obj


def get_cart_items(request: Request) -> dict:
    cart_items = Cart.objects.filter(Q(user=request.user.id) & Q(is_purchased=False)).values()
    return cart_items


def get_delivery_address(request: Request, id: int) -> Location:
    locations = Location.objects.filter(user=request.user).values()
    locations_list = list(locations)
    for location in locations_list:
        if location['id'] == id:
            loc_obj = Location.objects.get(id=id)
            return loc_obj


def get_product_billing_address(product_id: int) -> list:
    product_obj = Product.objects.get(id=product_id)
    bill_loc_obj = Location.objects.filter(user=product_obj.added_by).values()
    return list(bill_loc_obj)


def get_product_price(pk: int) -> float:
    prod_obj = Product.objects.get(id=pk)
    return prod_obj.price


def calculate_products_price_in_cart(request: Request) -> list:
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


def calculate_total_price(request: Request) -> float:
    products = calculate_products_price_in_cart(request)
    total_price = 0
    for product in products:
        total_price += product.get('price')

    return total_price


def get_product_id_and_quantity(ordered_items) -> list:
    product_id_quant_dict = []
    for item in ordered_items:
        d = {'id': item.get('id'), 'quantity': item.get('quantity')}
        product_id_quant_dict.append(d)
    return product_id_quant_dict


def insert_order_data_into_db(request: Request) -> int:
    id = request.data.get('delivery_address')
    if id is not None:
        loc_obj = get_delivery_address(request, id)
        if loc_obj is not None:
            print(loc_obj)
            data = {
                "ordered_items": calculate_products_price_in_cart(request),
                "total_price": calculate_total_price(request),
                "ordered_by": get_user_details(request),
                "delivery_address": loc_obj
            }
            try:
                Order.objects.create(**data)
                return 1
            except TypeError:
                return -1
        return 0
    else:
        return -1
