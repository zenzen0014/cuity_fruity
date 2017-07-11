from rest_framework import serializers
from .models import users, orders, menus, locations, wallets



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('__all__')
        #fields = ('user_id','type', 'mobile_no',)




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = ('__all__')
        #fields = ('order_id','store_id', 'customer_id', 'menu_list', 'order_status', 'time_stamp')




class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menus
        fields = ('__all__')
        # fields = ('menu_id', 'owner_id', 'menu_name', 'menu_detail', 'menu_img', 'price', 'menu_status')




class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = locations
        fields = ('__all__')
        # fields = ('location_id', 'l_user_id', 'location_name', 'lat', 'lng')




class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = wallets
        fields = ('__all__')
        # fields = ('trans_id', 'w_user_id', 'income', 'outcome', 'trans_date')



class Menu_User_Srlz(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(
    #     queryset=users.objects.all(),
    #     required=True,
    #     source='user',
    # )
    user = UserSerializer(read_only=False, required=False)
    class Meta:
        model = menus
        fields = ('menu_id', 'owner_id', 'menu_name', 'menu_img', 'price', 'menu_status', 'menu_detail', 'user')
