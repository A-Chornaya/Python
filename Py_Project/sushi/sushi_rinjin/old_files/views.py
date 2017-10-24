from django.shortcuts import render
from django.http import HttpResponse

'''from sushi_rinjin.models.menu import Menu


def index(request):
    context = {
        'menu_amount': Menu.objects.count()
    }
    return render(request, 'sushi_rinjin/index.html', context)


'''
def index(request):
    return HttpResponse("Hello, world!")
