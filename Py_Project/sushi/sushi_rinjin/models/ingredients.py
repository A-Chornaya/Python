from django.db import models
from django import forms
from django.forms import ModelForm
from rest_framework import serializers


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ingredient


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient']


class EditIngredForm(forms.Form):
    ingred_for_edit = forms.ModelChoiceField(
        queryset=Ingredients.objects.all(), empty_label=None,
        widget=forms.RadioSelect,
        label='Ingredients')


class IngredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'ingredient')
