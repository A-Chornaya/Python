from django import forms
from sushi_rinjin.models.ingredients import Ingredients
from django.contrib.auth.models import User
from sushi_rinjin.models.users_data import UsersDataProfile


class IngredInDishForm(forms.Form):
    ingredient = forms.ModelChoiceField(
        queryset=Ingredients.objects.all(), empty_label=None,
        widget=forms.RadioSelect, initial=1)


class PriceDishForm(forms.Form):
    price = forms.DecimalField(max_digits=4, decimal_places=2, initial=50)


class UserOrderForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  label='User', initial=1, empty_label=None)


class IngredDishForm(forms.Form):
    ingredient = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple)
