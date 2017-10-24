import django
#django.setup()

from sushi_rinjin.models.users_data import UsersData


def add_users():
    list_of_users = list()
    list_of_users.append(UsersData(user_name='Anastasiia', tel='0992365987',
                                   address='Artema str, 133/44'))
    list_of_users.append(UsersData(user_name='Daniil', tel='0506895623',
                                   address='Universitetskaya str, 201/65'))
    list_of_users.append(UsersData(user_name='Elene', tel='0956895632',
                                   address='Shevchenko str, 4a/36'))
    list_of_users.append(UsersData(user_name='Ekaterina', tel='0995632458',
                                   address='Shorsa str, 58/13'))
    list_of_users.append(UsersData(user_name='Evgeniya', tel='0956896325',
                                   address='Prohodchikov str, 132/96'))

    for obj in list_of_users:
        obj.save()

