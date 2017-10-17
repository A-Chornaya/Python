from django.db import models
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.menu import Menu


class OrderList(models.Model):
    order_id = models.ForeignKey(Order)
    dish_id = models.ForeignKey(Menu)
    amount = models.PositiveSmallIntegerField(default=1)
