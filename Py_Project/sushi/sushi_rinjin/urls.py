from django.conf.urls import url
from sushi_rinjin.views import view_index
from sushi_rinjin.views import view_menu
from sushi_rinjin.views import view_ingred
from sushi_rinjin.views import view_order

app_name = 'sushi_rinjin'

urlpatterns = [
    url(r'^$', view_index.index, name='index'),
    url(r'menu/', view_menu.index, name='menu'),
    url(r'ingredients/', view_ingred.index, name='ingredients'),
    url(r'orders/', view_order.index, name='orders'),
]
