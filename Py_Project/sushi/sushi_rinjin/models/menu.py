from django.db import models
from django.forms import ModelForm
from rest_framework import serializers
from django import forms
from sushi_rinjin.models.ingredients import Ingredients


class Menu(models.Model):
    dish_name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.dish_name


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {'ingredients': forms.CheckboxSelectMultiple}


class EditMenuForm(forms.Form):
    dish_for_edit = forms.ModelChoiceField(queryset=Menu.objects.all())


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
