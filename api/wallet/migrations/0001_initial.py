# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Their first name', max_length=60)),
                ('last_name', models.CharField(blank=True, help_text='Do you know it?', max_length=80)),
                ('slug', models.SlugField(blank=True)),
                ('proximity', models.PositiveSmallIntegerField(choices=[(0, 'Not sure'), ('Friends', ((10, 'Best friends forever'), (20, 'Close friends'), (30, 'Distant friends'), (40, 'Enemies til the end'))), ('Family', ((50, 'Super close'), (60, 'Only on occasion'), (70, 'Only at funerals'), (80, 'Family grouch!')))], help_text='How much of a distance to keep?')),
                ('email', models.EmailField(blank=True, help_text='Do they have an Email address?', max_length=254)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, help_text='File this person where?', null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.Category')),
            ],
            options={
                'ordering': ['last_name'],
                'verbose_name_plural': 'people',
            },
        ),
    ]