from django.http import HttpResponseRedirect
from sushi_rinjin.models.ingredients import Ingredients
from sushi_rinjin.models.ingredients import IngredientsForm
from sushi_rinjin.models.ingredients import EditIngredForm
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse


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


def choose_ingred(request):
    if request.method == 'POST':
        form_edit_ingred = EditIngredForm(request.POST)
        if form_edit_ingred.is_valid():
            ingred_for_edit = form_edit_ingred.cleaned_data['ingred_for_edit']
            if '_edit' in request.POST:
                return HttpResponseRedirect(reverse('sushi_rinjin:edit_ingred',
                                            args=(ingred_for_edit.id,)))
            if '_delete' in request.POST:
                ingred_for_edit.delete()
        return HttpResponseRedirect('/sushi_rinjin/ingredients/')
    else:
        form_edit_ingred = EditIngredForm()
        return render(request, 'sushi_rinjin/forms/choose_ingred.html',
                      {'form': form_edit_ingred})


def edit_ingred(request, id_ingred):
    ingred = Ingredients.objects.get(id=id_ingred)
    name_ingred = ingred.ingredient
    if request.method == 'POST':
        form_edit_ingred = IngredientsForm(request.POST, instance=ingred)
        if form_edit_ingred.is_valid():
            form_edit_ingred.save()
        return HttpResponseRedirect('/sushi_rinjin/ingredients/')
    else:
        form_edit_ingred = IngredientsForm(instance=ingred)
        return render(request, 'sushi_rinjin/forms/edit_ingred.html',
                      {'form': form_edit_ingred,
                       'id_ingred': id_ingred,
                       'name_ingred': name_ingred})
