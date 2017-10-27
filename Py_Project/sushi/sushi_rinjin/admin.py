from django.contrib import admin

from sushi_rinjin.models.ingredients import Ingredients
from sushi_rinjin.models.menu import Menu
from sushi_rinjin.models.users_data import UsersDataProfile
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.order_list import OrderList

admin.site.register(Ingredients)
admin.site.register(Menu)
admin.site.register(UsersDataProfile)
admin.site.register(Order)
admin.site.register(OrderList)
