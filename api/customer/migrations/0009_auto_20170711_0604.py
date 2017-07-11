# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_locations_wallets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='owner_id',
            field=models.OneToOneField(related_name='owner_id', to='customer.users'),
        ),
    ]
