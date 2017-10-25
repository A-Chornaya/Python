from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from sushi_rinjin.models.order import Order, OrderForm
from sushi_rinjin.models.order_list import OrderList, OrderListForm
#from django.views import generic
from django.urls import reverse
from django.contrib import messages


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
    cost = 0
    for order in order_list:
        cost += order.amount * order.dish_id.price
    context = {'id_order': id_order,
               'order_list': order_list,
               'cost': cost}
    return render(request, 'sushi_rinjin/order_detail.html', context)


def order_add(request):
    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            form_order.save()
        return HttpResponseRedirect('/sushi_rinjin/orders/')
    else:
        form_order = OrderForm()
        return render(request, 'sushi_rinjin/forms/order_add.html',
                      {'form': form_order})


def order_detail_add(request, id_order):
    if request.method == 'POST':
        form_order_detail = OrderListForm(request.POST)
        if form_order_detail.is_valid():
            amount = form_order_detail.cleaned_data['amount']
            if amount < 1:
                messages.error(request, 'Amount must be 1 or greater',
                               extra_tags='amount_error')
                return render(request, 'sushi_rinjin/forms/order_detail_add.html',
                      {'form': form_order_detail,
                       'id_order': id_order})
            form_detail = form_order_detail.save(commit=False)
            form_detail.order_id = Order.objects.get(id=id_order)

            form_detail.save()
        return HttpResponseRedirect(reverse('sushi_rinjin:detail', args=(
            id_order,)))
    else:
        form_order_detail = OrderListForm()
        return render(request, 'sushi_rinjin/forms/order_detail_add.html',
                      {'form': form_order_detail,
                       'id_order': id_order})


# class OrderFormCreate(generic.CreateView):
#     model = Order
#     fields = '__all__'
#     template_name = 'sushi_rinjin/forms/order_add.html'
#     success_url = '../../sushi_rinjin'
