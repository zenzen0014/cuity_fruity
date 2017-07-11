# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_logs_date', models.DateTimeField(auto_now_add=True)),
                ('c_uname', models.CharField(max_length=150)),
                ('c_is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('customer__c__id',),
            },
        ),
    ]
