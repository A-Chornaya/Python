from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.menu import Menu
from sushi_rinjin.models.menu import MenuSerializer
from sushi_rinjin.models.order import OrderSerializer
from sushi_rinjin.models.query import IngredInDishForm
from sushi_rinjin.models.query import PriceDishForm
from sushi_rinjin.models.query import UserOrderForm


def view_query(request):
    form_ingreds = IngredInDishForm()
    form_price = PriceDishForm()
    form_user_order = UserOrderForm()
    return render(request, 'sushi_rinjin/for_rest/queries_rest_form.html',
                  {'form_ingreds': form_ingreds,
                   'form_price': form_price,
                   'form_user_order': form_user_order})


@api_view(['GET'])
def user_orders(request, id_user):
    queryset = Order.objects.filter(user_id=id_user)
    serializer = OrderSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def less_price(request, price):
    queryset = Menu.objects.filter(price__lt=price)
    serializer = MenuSerializer(queryset, many=True)
    return Response(serializer.data)

