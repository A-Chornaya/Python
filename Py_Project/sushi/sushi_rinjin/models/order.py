from django.db import models
from django.forms import ModelForm
#from sushi_rinjin.models.users_data import UsersDataProfile
from rest_framework import serializers
from django.contrib.auth.models import User


class Order(models.Model):
    PAY_METHOD_CHOISES = (
        ('cash', 'cash'),
        ('credit card', 'credit card'),
        ('check', 'check'),
    )
    pay_method = models.CharField(max_length=15, choices=PAY_METHOD_CHOISES,
                                  default='cash')
    #user_id = models.ForeignKey(UsersDataProfile)
    user_id = models.ForeignKey(User)
    pay = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    def pay_or_not(self):
        if self.pay:
            result = 'paid'
        else:
            result = 'not paid'
        return result


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user_id', 'pay_method', 'pay']
        labels = {'user_id': 'User'}


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
