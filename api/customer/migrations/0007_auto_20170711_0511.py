# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20170711_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='menus',
            fields=[
                ('menu_id', models.AutoField(serialize=False, primary_key=True)),
                ('menu_name', models.CharField(max_length=50)),
                ('menu_detail', models.CharField(max_length=200)),
                ('menu_img', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('menu_status', models.CharField(max_length=20)),
                ('owner_id', models.ForeignKey(related_name='owner_id', to='customer.users')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('menu_list', models.CharField(max_length=20)),
                ('order_status', models.CharField(max_length=20)),
                ('time_stamp', models.DateField()),
                ('customer_id', models.ForeignKey(related_name='customer_id', to='customer.users')),
                ('store_id', models.ForeignKey(related_name='store_id', to='customer.users')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='store_id',
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]
