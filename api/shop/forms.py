from django import forms

from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('order_id','store_id', 'customer_id', 'menu_list', 'time_stamp', 'status')