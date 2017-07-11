# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20170711_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='owner_id',
            field=models.ForeignKey(related_name='owner_id', db_column='owner_id', to='customer.users'),
        ),
    ]
