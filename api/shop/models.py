from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Orders(models.Model):
	order_id		= models.AutoField(primary_key=True)#models.IntegerField(primary_key=True)
	store_id 		= models.CharField(max_length=50)
	customer_id		= models.CharField(max_length=50)
	menu_list 		= models.CharField(max_length=50)#models.PositiveSmallIntegerField(choices=list_menu, blank=True, null=True)
	time_stamp		= models.DateField(blank=True, null=True)
	status 			= models.CharField(max_length=50)