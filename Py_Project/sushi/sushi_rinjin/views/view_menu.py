from django.shortcuts import render
from sushi_rinjin.models.menu import Menu


def index(request):
    list_of_dishes = Menu.objects.all()
    context = {'dishes': list_of_dishes}
    return render(request, 'sushi_rinjin/menu.html', context)
