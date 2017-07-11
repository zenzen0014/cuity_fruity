# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20170711_0511'),
    ]

    operations = [
        migrations.CreateModel(
            name='locations',
            fields=[
                ('location_id', models.AutoField(serialize=False, primary_key=True)),
                ('location_name', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
                ('l_user_id', models.ForeignKey(related_name='l_user_id', to='customer.users')),
            ],
        ),
        migrations.CreateModel(
            name='wallets',
            fields=[
                ('trans_id', models.AutoField(serialize=False, primary_key=True)),
                ('income', models.IntegerField()),
                ('outcome', models.IntegerField()),
                ('trans_date', models.DateField()),
                ('w_user_id', models.ForeignKey(related_name='w_user_id', to='customer.users')),
            ],
        ),
    ]
