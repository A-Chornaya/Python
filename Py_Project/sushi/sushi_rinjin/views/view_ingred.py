from django.shortcuts import render
from sushi_rinjin.models.ingredients import Ingredients


def index(request):
    list_of_ingreds = Ingredients.objects.all()
    context = {'ingred_list': list_of_ingreds}
    return render(request, 'sushi_rinjin/ingredients.html', context)
