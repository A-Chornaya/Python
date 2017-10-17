import django
django.setup()

from sushi_rinjin.models.order import Order
from sushi_rinjin.models.users_data import UsersData


def add_orders():
    order1 = Order(pay_method='cash', user_id=UsersData.objects.get(id='1'),
                   pay=True)
    order2 = Order(pay_method='credit card', user_id=UsersData.objects.get(
        id='2'),
                   pay=True)
    order3 = Order(user_id=UsersData.objects.get(id='4'),
                   pay=False)

    order1.save()
    order2.save()
    order3.save()


add_orders()
