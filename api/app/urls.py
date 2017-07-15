from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .models import *
from .views import *

urlpatterns = [
################# models #################
    url(r'^$', index),
    url(r'^get_order_on_hand$', get_order_on_hand),
    url(r'^get_supplier_order_history$', get_supplier_order_history),
    url(r'^get_supplier_order_history_detail$', get_supplier_order_history_detail),



    url(r'^order_on_hand_confirm$', order_on_hand_confirm),

    url(r'^update_delivery_task_finder$', update_delivery_task_finder),

    url(r'^confirm_supplier_on_hand$', confirm_supplier_on_hand),

    url(r'^get_supplier_on_hand$', get_supplier_on_hand),

    
    url(r'^get_supplier_menu_list$', get_supplier_menu_list),

    url(r'^update_menu_supplier$', update_menu_supplier),


    url(r'^get_customer_order_history$', get_customer_order_history), 

    url(r'^get_customer_order_history_detail$', get_customer_order_history_detail), 
    


    url(r'^get_supplier_on_hand_detail$', get_supplier_on_hand_detail),


    url(r'^delivery_collect_money$', delivery_collect_money),


    url(r'^get_delivery_task_on_hand$', get_delivery_task_on_hand),

    url(r'^get_delivery_task_finder$', get_delivery_task_finder),

    
    url(r'^get_delivery_task_history$', get_delivery_task_history),


    url(r'^get_customer_order_status$', get_customer_order_status),
    


    url(r'^test_new_user$', test_new_user),

################# models #################





################# views #################
    url(r'^supplier$', supplier),
    url(r'^delivery$', delivery),
    url(r'^customer$', customer),


    url(r'^test_get$', test_get),
    url(r'^test_post$', test_post),
################# views #################
]