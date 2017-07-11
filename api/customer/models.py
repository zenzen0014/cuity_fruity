# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class users(models.Model):
    user_id     = models.AutoField(primary_key=True)
    type        = models.CharField(max_length=20)
    mobile_no   = models.CharField(max_length=24)
    def __str__(self):
        return self.user_id

class orders(models.Model):
    order_id        = models.AutoField(primary_key=True)
    store_id        = models.ForeignKey(users, on_delete=models.CASCADE, related_name="store_id")
    customer_id     = models.ForeignKey(users, on_delete=models.CASCADE, related_name="customer_id")
    menu_list       = models.CharField(max_length=20)
    order_status    = models.CharField(max_length=20)
    time_stamp      = models.DateField()
    def __str__(self):
        return self.time_stamp

class menus(models.Model):
    menu_id         = models.AutoField(primary_key=True)
    owner_id        = models.ForeignKey(users, on_delete=models.CASCADE, related_name="owner_id", db_column='owner_id')
    menu_name       = models.CharField(max_length=50)
    menu_detail     = models.CharField(max_length=200)
    menu_img        = models.CharField(max_length=64)
    price           = models.IntegerField()
    menu_status     = models.CharField(max_length=20)
    # def __str__(self):
    #     return self.menu_status

class locations(models.Model):
    location_id     = models.AutoField(primary_key=True)
    l_user_id       = models.ForeignKey(users, on_delete=models.CASCADE, related_name="l_user_id")
    location_name   = models.CharField(max_length=50)
    lat             = models.CharField(max_length=20)
    lng             = models.CharField(max_length=20)


class wallets(models.Model):
    trans_id        = models.AutoField(primary_key=True)
    w_user_id       = models.ForeignKey(users, on_delete=models.CASCADE, related_name="w_user_id")
    income          = models.IntegerField()
    outcome         = models.IntegerField()
    trans_date      = models.DateField()