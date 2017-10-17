from django.conf.urls import url
from sushi_rinjin.views import index

app_name = 'sushi_rinjin'

urlpatterns = [
    url(r'^$', index.index, name='index'),
]
