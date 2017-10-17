from django.shortcuts import render
from sushi_rinjin.models.menu import Menu


def index(request):
    context = {
        'menu_amount': Menu.objects.count()
    }
    return render(request, 'sushi_rinjin/index.html', context)
