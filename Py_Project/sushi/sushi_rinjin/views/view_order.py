from django.http import Http404
from django.shortcuts import render
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.order_list import OrderList


def index(request):
    try:
        orders = Order.objects.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

    result_list = list()
    for ord in orders:
        user = ord.user_id.user_name
        result_list.append([ord.id, user, ord.pay_or_not, ord.pay_method])

    return render(request, 'sushi_rinjin/orders.html',
                  {'result_list': result_list})


def detail(request, id_order):
    try:
        order_list = OrderList.objects.filter(order_id=id_order)
    except Order.DoesNotExist:
        raise Http404("Order does not exist")
    context = {'id_order': id_order,
               'order_list': order_list}
    return render(request, 'sushi_rinjin/order_detail.html', context)
