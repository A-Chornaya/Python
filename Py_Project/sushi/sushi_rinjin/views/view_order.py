from django.shortcuts import render
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.order_list import OrderList


def index(request):
    orders = Order.objects.all()
    result_list = list()

    for ord in orders:
        user = ord.user_id.user_name
        list_order = list()
        for obj_list in OrderList.objects.filter(order_id=ord.id):
            list_order.append(obj_list.dish_id.dish_name)
        result_list.append([ord.id, user, list_order])
    context = {'result_list': result_list}
    return render(request, 'sushi_rinjin/orders.html', context)
