from django.db import models
from sushi_rinjin.models.ingredients import Ingredients


class Menu(models.Model):
    dish_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredients)
