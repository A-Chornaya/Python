import django
django.setup()

from sushi_rinjin.models.menu import Menu
from sushi_rinjin.models.ingredients import Ingredients


def add_menu():
    ingrid1 = Ingredients.objects.get(id='1')
    ingrid2 = Ingredients.objects.get(id='2')
    ingrid3 = Ingredients.objects.get(id='5')
    ingrid4 = Ingredients.objects.get(id='6')
    ingrid5 = Ingredients.objects.get(id='7')
    ingrid6 = Ingredients.objects.get(id='8')
    ingrid8 = Ingredients.objects.get(id='10')
    ingrid9 = Ingredients.objects.get(id='11')
    ingrid17 = Ingredients.objects.get(id='19')
    ingrid18 = Ingredients.objects.get(id='20')
    ingrid11 = Ingredients.objects.get(id='13')
    ingrid13 = Ingredients.objects.get(id='15')
    ingrid19 = Ingredients.objects.get(id='21')

    dish1 = Menu(dish_name='Rolls Filadelfia', price=60.00)
    dish1.save()
    dish1.ingredients.add(ingrid1, ingrid2, ingrid5, ingrid13)

    dish2 = Menu(dish_name='Rolls Kalifornia', price=70.00)
    dish2.save()
    dish2.ingredients.add(ingrid1, ingrid2, ingrid4, ingrid11, ingrid17,
                          ingrid18)

    dish3 = Menu(dish_name='Rolls Eel', price=80.00)
    dish3.save()
    dish3.ingredients.add(ingrid1, ingrid2, ingrid6, ingrid19)

    dish4 = Menu(dish_name='Sushi Squid', price=15.00)
    dish4.save()
    dish4.ingredients.add(ingrid1, ingrid9, ingrid3)

    dish5 = Menu(dish_name='Sushi Shrimp', price=10.00)
    dish5.save()
    dish5.ingredients.add(ingrid1, ingrid8, ingrid3)


add_menu()
