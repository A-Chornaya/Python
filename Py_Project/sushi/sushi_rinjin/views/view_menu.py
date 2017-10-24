from django.shortcuts import render
from django.http import HttpResponseRedirect
from sushi_rinjin.models.menu import Menu, MenuForm


def index(request):
    list_of_dishes = Menu.objects.all()
    context = {'dishes': list_of_dishes}
    return render(request, 'sushi_rinjin/menu.html', context)


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
