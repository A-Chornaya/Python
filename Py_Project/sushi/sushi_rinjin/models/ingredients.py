from django.db import models
from django.forms import ModelForm


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ingredient


class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient']
