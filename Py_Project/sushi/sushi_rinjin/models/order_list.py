from django.db import models
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.menu import Menu
from django.forms import ModelForm


class OrderList(models.Model):
    order_id = models.ForeignKey(Order)
    dish_id = models.ForeignKey(Menu)
    amount = models.PositiveSmallIntegerField(default=1)


class OrderListForm(ModelForm):
    class Meta:
        model = OrderList
        fields = ['dish_id', 'amount']
        labels = {'dish_id': 'Dish'}