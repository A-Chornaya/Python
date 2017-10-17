import django
django.setup()

from sushi_rinjin.models.ingredients import Ingredients




def add_ingredients():
    list_of_ingredients = list()
    list_of_ingredients.append(Ingredients(ingredient='rice'))
    list_of_ingredients.append(Ingredients(ingredient='nori'))
    list_of_ingredients.append(Ingredients(ingredient='soy sauce'))
    list_of_ingredients.append(Ingredients(ingredient='wasabi'))
    list_of_ingredients.append(Ingredients(ingredient='salmon'))
    list_of_ingredients.append(Ingredients(ingredient='eel'))
    list_of_ingredients.append(Ingredients(ingredient='tuna'))
    list_of_ingredients.append(Ingredients(ingredient='shrimp'))
    list_of_ingredients.append(Ingredients(ingredient='squid'))
    list_of_ingredients.append(Ingredients(ingredient='crab'))
    list_of_ingredients.append(Ingredients(ingredient='crab sticks'))
    list_of_ingredients.append(Ingredients(ingredient='teriyaki sauce'))
    list_of_ingredients.append(Ingredients(ingredient='cheese creamy'))
    list_of_ingredients.append(Ingredients(ingredient='red caviar'))
    list_of_ingredients.append(Ingredients(ingredient='tobiko caviar'))
    list_of_ingredients.append(Ingredients(ingredient='shiitake mushrooms'))
    list_of_ingredients.append(Ingredients(ingredient='cucumber'))
    list_of_ingredients.append(Ingredients(ingredient='avokado'))
    list_of_ingredients.append(Ingredients(ingredient='tofu'))
    list_of_ingredients.append(Ingredients(ingredient='mayonnaise'))

    for obj in list_of_ingredients:
        obj.save()


add_ingredients()
