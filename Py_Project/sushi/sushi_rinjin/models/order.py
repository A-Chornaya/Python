from django.db import models
from sushi_rinjin.models.payment_method import PaymentMethod
from sushi_rinjin.models.users_data import UsersData


class Order(models.Model):
    pay = models.BooleanField(default=False)
    pay_method_id = models.ForeignKey(PaymentMethod)
    user_id = models.ForeignKey(UsersData)
