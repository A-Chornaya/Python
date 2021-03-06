from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from sushi_rinjin.models.menu import Menu
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.order_list import OrderList
from sushi_rinjin.models.query import IngredDishForm
from sushi_rinjin.models.query import PriceDishForm
from sushi_rinjin.models.query import UserOrderForm


def list_query(request):
    if request.method == 'POST':
        form_ingreds = IngredDishForm(request.POST)
        form_price = PriceDishForm(request.POST)
        form_user_order = UserOrderForm(request.POST)
        if '_ingreds' in request.POST:
            if form_ingreds.is_valid():
                some_ingred = form_ingreds.cleaned_data['ingredient']
                # get dishes that have all ingredients from checkbox_list
                q_menu = list()
                for ingred in some_ingred:
                    q_menu.append(Menu.objects.filter(ingredients=ingred))
                    dishes = Menu.objects.all()
                for q in q_menu:
                    dishes = dishes.intersection(q)
                return render(request,
                              'sushi_rinjin/queries/ingred_in_menu.html',
                              {'dishes': dishes,
                               'ingred_name': tuple(some_ingred.values_list(
                                   'ingredient'))})
            else:
                return HttpResponseRedirect(reverse_lazy(
                    'sushi_rinjin:query_list'))

        if '_price' in request.POST:
            if form_price.is_valid():
                some_price = form_price.cleaned_data['price']
                dishes = Menu.objects.filter(price__lt=some_price)
                return render(request,
                              'sushi_rinjin/queries/price_in_menu.html',
                              {'dishes': dishes,
                               'price': some_price})
        if '_user_order' in request.POST:
            if form_user_order.is_valid():
                user = form_user_order.cleaned_data['user']
                user_orders = Order.objects.filter(user_id=user.id)
                # calculate costs of each order and total cost all orders
                list_order_cost = list()
                total_cost = 0
                for obj in user_orders:
                    order_list = OrderList.objects.filter(order_id=obj.id)
                    cost = 0
                    for order in order_list:
                        cost += order.amount * order.dish_id.price
                    list_order_cost.append((obj.id, cost))
                    total_cost += cost
                return render(request,
                              'sushi_rinjin/queries/user_orders.html',
                              {'user_name': user.usersdataprofile.full_name(),
                               'user_orders': list_order_cost,
                               'total_cost': total_cost})
    else:
        form_ingreds = IngredDishForm()
        form_price = PriceDishForm()
        form_user_order = UserOrderForm()
        return render(request, 'sushi_rinjin/forms/queries_form.html',
                      {'form_ingreds': form_ingreds,
                       'form_price': form_price,
                       'form_user_order': form_user_order})
