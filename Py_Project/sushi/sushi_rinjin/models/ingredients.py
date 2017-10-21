from django.db import models


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)

    @property
    def __str__(self):
        return self.ingredient
