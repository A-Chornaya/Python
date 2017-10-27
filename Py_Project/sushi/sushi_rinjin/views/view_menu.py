from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from sushi_rinjin.models.menu import Menu
from sushi_rinjin.models.menu import MenuForm
from sushi_rinjin.models.menu import EditMenuForm



def index(request):
    list_of_dishes = Menu.objects.all()
    context = {'dishes': list_of_dishes}
    return render(request, 'sushi_rinjin/menu.html', context)


@login_required
def dish_add(request):
    if request.method == 'POST':
        form_menu = MenuForm(request.POST)
        if form_menu.is_valid():
            form_menu.save()
        return HttpResponseRedirect('/sushi_rinjin/menu/')
    else:
        form_menu = MenuForm()
        return render(request, 'sushi_rinjin/forms/dish_add.html',
                      {'form': form_menu})


@login_required
def edit_menu(request):
    if request.method == 'POST':
        form_edit_menu = EditMenuForm(request.POST)
        if form_edit_menu.is_valid():
            dish_for_edit = form_edit_menu.cleaned_data['dish_for_edit']
            if '_edit' in request.POST:
                return HttpResponseRedirect(reverse('sushi_rinjin:edit_dish',
                                            args=(dish_for_edit.id,)))
            if '_delete' in request.POST:
                #dish_for_edit.ingredients.clear()
                dish_for_edit.delete()
        return HttpResponseRedirect('/sushi_rinjin/menu/')
    else:
        form_edit_menu = EditMenuForm()
        return render(request, 'sushi_rinjin/forms/edit_menu.html',
                      {'form': form_edit_menu})


@login_required
def edit_dish(request, id_dish):
    dish = Menu.objects.get(id=id_dish)
    name_dish = dish.dish_name
    if request.method == 'POST':
        form_edit_dish = MenuForm(request.POST, instance=dish)
        if form_edit_dish.is_valid():
            form_edit_dish.save()
        return HttpResponseRedirect('/sushi_rinjin/menu/')
    else:
        form_edit_dish = MenuForm(instance=dish)
        return render(request, 'sushi_rinjin/forms/edit_dish.html',
                      {'form': form_edit_dish,
                       'id_dish': id_dish,
                       'name_dish': name_dish})
