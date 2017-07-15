# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class users(models.Model):
    user_id     = models.AutoField(primary_key=True)
    user_name   = models.CharField(max_length=50)
    type        = models.CharField(max_length=20)
    mobile_no   = models.CharField(max_length=24)
    def __str__(self):
        return self.user_id

class orders(models.Model):
    order_id                = models.IntegerField()
    menu_id                 = models.CharField(max_length=20)
    class Meta: 
        unique_together =(("order_id","menu_id"))
    store_id                = models.ForeignKey(users, on_delete=models.CASCADE, related_name="store_id")
    customer_id             = models.ForeignKey(users, on_delete=models.CASCADE, related_name="customer_id")
    store_location_id       = models.ForeignKey('locations', on_delete=models.CASCADE, related_name="store_location_id")
    customer_location_id    = models.ForeignKey('locations', on_delete=models.CASCADE, related_name="customer_location_id")
    order_size              = models.CharField(max_length=50)
    order_status            = models.CharField(max_length=20)
    delivery_status         = models.CharField(max_length=20)
    delivery_id             = models.CharField(max_length=20)
    size                    = models.CharField(max_length=20)
    amount                  = models.IntegerField()
    time_stamp              = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.time_stamp

class menus(models.Model):
    menu_id         = models.IntegerField()
    menu_size       = models.CharField(max_length=20)
    class Meta: 
        unique_together=(("menu_id","menu_size"))
    owner_id        = models.ForeignKey(users, on_delete=models.CASCADE, related_name="owner_id", db_column='owner_id')
    menu_name       = models.CharField(max_length=50)
    menu_detail     = models.CharField(max_length=200)
    menu_img        = models.CharField(max_length=64)
    price           = models.CharField(max_length=24)
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
    trans_date      = models.DateField(auto_now_add=True)