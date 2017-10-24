import django
django.setup()

from sushi_rinjin.scripts_for_DB.script_ingredients import add_ingredients
from sushi_rinjin.scripts_for_DB.script_menu import add_menu
from sushi_rinjin.scripts_for_DB.script_users_data import add_users
from sushi_rinjin.scripts_for_DB.script_order import add_orders
from sushi_rinjin.scripts_for_DB.script_order_list import add_order_list

add_ingredients()
add_menu()
add_users()
add_orders()
add_order_list()
