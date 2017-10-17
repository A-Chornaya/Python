# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dish_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('ingredients', models.ManyToManyField(to='sushi_rinjin.Ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay_method', models.CharField(default=b'CASH', max_length=15, choices=[(b'CASH', b'cash'), (b'CREDIT', b'credit card'), (b'CHECK', b'check')])),
                ('pay', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveSmallIntegerField(default=1)),
                ('dish_id', models.ForeignKey(to='sushi_rinjin.Menu')),
                ('order_id', models.ForeignKey(to='sushi_rinjin.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay_method', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UsersData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(to='sushi_rinjin.UsersData'),
        ),
    ]
