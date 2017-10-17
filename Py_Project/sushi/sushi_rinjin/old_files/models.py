from django.db import models
#from sushi_rinjin.model import *


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)

    @property
    def __str__(self):
        return self.ingredient


class Menu(models.Model):
    dish_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredients)


#class PaymentMethod(models.Model):
#    pay_method = models.CharField(max_length=50)


class UsersData(models.Model):
    user_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=25)
    address = models.CharField(max_length=50)


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


class OrderList(models.Model):
    order_id = models.ForeignKey(Order)
    dish_id = models.ForeignKey(Menu)
    amount = models.PositiveSmallIntegerField(default=1)

