import django
django.setup()

from sushi_rinjin.models.order_list import OrderList
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.menu import Menu


def add_order_list():
    list_of_orders = list()
    order1 = Order.objects.get(id='1')
    order2 = Order.objects.get(id='2')
    order3 = Order.objects.get(id='3')

    dish1 = Menu.objects.get(id='1')
    dish2 = Menu.objects.get(id='2')
    dish3 = Menu.objects.get(id='3')
    dish4 = Menu.objects.get(id='5')

    list_of_orders.append(OrderList(order_id=order1, dish_id=dish1, amount=2))
    list_of_orders.append(OrderList(order_id=order2, dish_id=dish2))
    list_of_orders.append(OrderList(order_id=order2, dish_id=dish3, amount=1))
    list_of_orders.append(OrderList(order_id=order2, dish_id=dish4, amount=4))
    list_of_orders.append(OrderList(order_id=order3, dish_id=dish1, amount=2))
    list_of_orders.append(OrderList(order_id=order3, dish_id=dish3))

    for obj in list_of_orders:
        obj.save()


add_order_list()
