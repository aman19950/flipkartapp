from math import prod
from django import template

from ..models import *

register = template.Library()


@register.filter(name="is_exist_in_cart")
def is_exist_in_cart(product, cart):
    key = cart.keys()
    for id in key:
        if int(id) == product.id:
            return True
    return False


@register.filter(name="cartquantity")
def cartquantity(product, cart):
    key = cart.keys()
    for id in key:
        if int(id) == product.id:
            return cart.get(id)
    return False


@register.filter(name="Total_price")
def Total_price(product, cart):
    item_price = product.price * cartquantity(product, cart)
    return item_price


@register.filter(name="payable_price")
def payable_price(product, cart):
    s = 0
    print(s)
    for i in product:
        print(i)
        s = s + Total_price(i, cart)
    return s


@register.filter(name="order_amount")
def order_amount(num1, num2):
    return num1*num2
