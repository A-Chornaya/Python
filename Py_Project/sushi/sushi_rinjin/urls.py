from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from sushi_rinjin.views import view_index
from sushi_rinjin.views import view_menu
from sushi_rinjin.views import view_ingred
from sushi_rinjin.views import view_order
from sushi_rinjin.views import view_queries
from sushi_rinjin.views import view_queries_rest
from sushi_rinjin.views import view_user
from sushi_rinjin.views import view_ingred_rest
from sushi_rinjin.views import view_order_rest

app_name = 'sushi_rinjin'

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name':
        'sushi_rinjin/registration/login.html'}, name='login'),
    url(r'^accounts/logout$', auth_views.logout,
        {'next_page': '/sushi_rinjin/'}, name='logout'),
    url(r'^accounts/signin$', view_user.signup, name='signup'),
    url(r'^$', view_index.index, name='index'),

    url(r'^ingredients/$', view_ingred.index, name='ingredients'),
    url(r'^ingredients/add/$', view_ingred.ingred_add, name='add_ingred'),
    url(r'^ingredients/edit/$', view_ingred.choose_ingred,
        name='choose_ingred'),
    url(r'^ingredients/edit/(?P<id_ingred>[0-9]+)/$', view_ingred.edit_ingred,
        name='edit_ingred'),
    url(r'^ingred/$', view_ingred_rest.IngredList.as_view(),
        name='ingred'),
    url(r'^ingred_rest/$', view_ingred_rest.ingred_rest, name='ingred_rest'),

    url(r'^menu/$', view_menu.index, name='menu'),
    url(r'^dish_add/$', view_menu.dish_add, name='add_dish'),
    url(r'^menu/edit/$', view_menu.edit_menu, name='edit_menu'),
    url(r'^menu/edit/(?P<id_dish>[0-9]+)/$', view_menu.edit_dish,
        name='edit_dish'),

    url(r'^orders/$', view_order.index, name='orders'),
    url(r'^order/(?P<id_order>[0-9]+)/$', view_order.detail, name='detail'),

    url(r'^order_add/$', view_order.order_add,
        name='order_add'),
    url(r'^order/(?P<id_order>[0-9]+)/add$', view_order.order_detail_add,
        name='order_detail_add'),
    url(r'^order/(?P<id_order>[0-9]+)/edit$',
        view_order_rest.OrderEdit.as_view(), name='order_edit'),
    url(r'^order/(?P<id_order>[0-9]+)/detail/(?P<order_list_id>[0-9]+)/edit/$',
        view_order_rest.OrderDetailEdit.as_view(),
        name='order_detail_edit'),

    url(r'^queries/$', view_queries.list_query, name='query_list'),
    url(r'^queries_rest/$', view_queries_rest.view_query, name='query_rest'),
    url(r'^queries_rest/user_orders/(?P<id_user>[0-9]+)$',
        view_queries_rest.user_orders, name='query_rest_user'),
    url(r'^queries_rest/price/(?P<price>[0-9]+)$',
        view_queries_rest.less_price, name='query_rest_price'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
