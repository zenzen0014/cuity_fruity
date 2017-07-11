# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('store_id', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('menu_list', models.CharField(max_length=50)),
                ('time_stamp', models.DateField(null=True, blank=True)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
