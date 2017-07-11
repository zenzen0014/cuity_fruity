# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20170711_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('menu_list', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('time_stamp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=24)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(related_name='customer_id', to='customer.users'),
        ),
        migrations.AddField(
            model_name='order',
            name='store_id',
            field=models.ForeignKey(related_name='store_id', to='customer.users'),
        ),
    ]
