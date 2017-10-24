import django
#django.setup()

from sushi_rinjin.models.menu import Menu
from sushi_rinjin.models.ingredients import Ingredients


def add_menu():
    rice = Ingredients.objects.get(ingredient='rice')
    nori = Ingredients.objects.get(ingredient='nori')
    soy = Ingredients.objects.get(ingredient='soy sauce')
    wasabi = Ingredients.objects.get(ingredient='wasabi')
    salmon = Ingredients.objects.get(ingredient='salmon')
    eel = Ingredients.objects.get(ingredient='eel')
    shrimp = Ingredients.objects.get(ingredient='shrimp')
    squid = Ingredients.objects.get(ingredient='squid')
    cucumber = Ingredients.objects.get(ingredient='cucumber')
    avokado = Ingredients.objects.get(ingredient='avokado')
    crab_stick = Ingredients.objects.get(ingredient='crab sticks')
    cheese_cream = Ingredients.objects.get(ingredient='cheese creamy')
    tofu = Ingredients.objects.get(ingredient='tofu')

    dish1 = Menu(dish_name='Rolls Filadelfia', price=60.00)
    dish1.save()
    dish1.ingredients.add(rice, nori, salmon, cheese_cream)

    dish2 = Menu(dish_name='Rolls Kalifornia', price=70.00)
    dish2.save()
    dish2.ingredients.add(rice, nori, wasabi, crab_stick, cucumber,
                          avokado)

    dish3 = Menu(dish_name='Rolls Eel', price=80.00)
    dish3.save()
    dish3.ingredients.add(rice, nori, eel, tofu)

    dish4 = Menu(dish_name='Sushi Squid', price=15.00)
    dish4.save()
    dish4.ingredients.add(rice, squid, soy)

    dish5 = Menu(dish_name='Sushi Shrimp', price=10.00)
    dish5.save()
    dish5.ingredients.add(rice, shrimp, soy)

