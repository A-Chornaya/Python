from django.conf.urls import url
from sushi_rinjin.views import view_index
from sushi_rinjin.views import view_menu

app_name = 'sushi_rinjin'

urlpatterns = [
    url(r'^$', view_index.index, name='index'),
    url(r'menu/', view_menu.index, name='menu'),
]
