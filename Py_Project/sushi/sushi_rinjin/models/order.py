from django.db import models
from sushi_rinjin.models.payment_method import PaymentMethod
from sushi_rinjin.models.users_data import UsersData


class Order(models.Model):
    PAY_METHOD_CHOISES = (
        ('CASH', 'cash'),
        ('CREDIT', 'credit card'),
        ('CHECK', 'check'),
    )
    pay_method = models.CharField(max_length=15, choices=PAY_METHOD_CHOISES,
                                  default='cash')
    user_id = models.ForeignKey(UsersData)
    pay = models.BooleanField(default=False)
