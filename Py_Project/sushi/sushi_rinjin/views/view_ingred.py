from django.http import HttpResponseRedirect
from sushi_rinjin.models.ingredients import Ingredients, IngredientsForm
from django.shortcuts import render
from django.contrib import messages


def index(request):
    list_of_ingreds = Ingredients.objects.all()
    context = {'ingred_list': list_of_ingreds}
    return render(request, 'sushi_rinjin/ingredients.html', context)


def ingred_add(request):
    if request.method == 'POST':
        form_ingred= IngredientsForm(request.POST)
        if form_ingred.is_valid():
            form_ingred.save()
            messages.success(request, 'A new ingredient added successfully')
        return HttpResponseRedirect('/sushi_rinjin/ingredients/')
    else:
        form_ingred = IngredientsForm()
        return render(request, 'sushi_rinjin/forms/ingredient_add.html',
                      {'form': form_ingred})
