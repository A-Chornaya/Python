from django.contrib import admin

from .models.ingredients import Ingredients
from .models.menu import Menu
from .models.users_data import UsersData
from .models.order import Order
from .models.order_list import OrderList

admin.site.register(Ingredients)
admin.site.register(Menu)
admin.site.register(UsersData)
admin.site.register(Order)
admin.site.register(OrderList)
