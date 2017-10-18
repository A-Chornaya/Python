from django.shortcuts import render
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.order_list import OrderList



def index(request):
    orders = Order.objects.all()
    order_list_list = list()
    #result_list = list()
    for ord in orders:
        list_order = list()
        for obj_list in OrderList.objects.filter(order_id=ord.id):
            list_order.append(obj_list.dish_id.dish_name)
        order_list_list.append(list_order)
        #result_list.append([ord.id, ])
    context = {'orders': [(order.id, Order.objects.filter(
                   id=order.id).values('id', 'user_id__user_name'))
                          for order in Order.objects.all()],
               'order_list_list': order_list_list}
    return render(request, 'sushi_rinjin/orders.html', context)
