from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from sushi_rinjin.views import view_index
from sushi_rinjin.views import view_menu
from sushi_rinjin.views import view_ingred
from sushi_rinjin.views import view_order
from sushi_rinjin.views import view_queries
from sushi_rinjin.views import view_user
from sushi_rinjin.views import view_ingred_rest

app_name = 'sushi_rinjin'

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name':
        'sushi_rinjin/registration/login.html'}, name='login'),
    url(r'^accounts/logout$', auth_views.logout,
        {'next_page': '/sushi_rinjin/'}, name='logout'),
    url(r'^accounts/signin$', view_user.signup, name='signup'),
    url(r'^$', view_index.index, name='index'),
    url(r'^menu/$', view_menu.index, name='menu'),
    url(r'^ingredients/$', view_ingred.index, name='ingredients'),
    url(r'^orders/$', view_order.index, name='orders'),
    url(r'^order/(?P<id_order>[0-9]+)/$', view_order.detail, name='detail'),
    url(r'^ingredients/add/$', view_ingred.ingred_add, name='add_ingred'),
    url(r'^dish_add/$', view_menu.dish_add, name='add_dish'),
    url(r'^order_add/$', view_order.order_add,
        name='order_add'),
    url(r'^order/(?P<id_order>[0-9]+)/add$', view_order.order_detail_add,
        name='order_detail_add'),
    url(r'^menu/edit/$', view_menu.edit_menu, name='edit_menu'),
    url(r'^menu/edit/(?P<id_dish>[0-9]+)/$', view_menu.edit_dish,
        name='edit_dish'),
    url(r'^ingredients/edit/$', view_ingred.choose_ingred, name='choose_ingred'),
    url(r'^ingredients/edit/(?P<id_ingred>[0-9]+)/$', view_ingred.edit_ingred,
        name='edit_ingred'),
    url(r'^queries/$', view_queries.list_query, name='query_list'),

    url(r'^ingred/$', view_ingred_rest.IngredList.as_view(),
        name='ingred'),
    url(r'^ingred/(?P<pk>[0-9]+)/$', view_ingred_rest.IngredDetail.as_view(),
        name='ingred_redact_rest'),
    url(r'^ingred_rest/$', view_ingred_rest.ingred_rest, name='ingred_rest'),

]

urlpatterns = format_suffix_patterns(urlpatterns)