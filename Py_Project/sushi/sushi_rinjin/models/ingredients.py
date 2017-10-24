from django.db import models
from django import forms
from django.forms import ModelForm


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ingredient


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient']


class EditIngredForm(forms.Form):
    # list_ing = list()
    # for obj in Ingredients.objects.all():
    #     list_ing.append([obj.ingredient, obj.ingredient])
    ingred_for_edit = forms.ModelChoiceField(
         queryset=Ingredients.objects.all())
    #ingred_for_edit = forms.Select(choices=tuple(list_ing))
