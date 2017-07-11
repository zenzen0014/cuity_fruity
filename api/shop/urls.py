from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views

urlpatterns = [

	url(r'^$', views.order_lists, name="order_lists"), #ListCustomer customer_list
	

	url(r'^order_add$', views.order_add, name="order_add"),
	url(r'^order_add_form$', views.order_add_form, name="order_add_form"),

	url(r'^order_create_form_ajax$', views.order_create_form_ajax, name="order_create_form_ajax"),
	url(r'^order_update_form_ajax/(?P<pk>\d+)$', views.order_update_form_ajax, name='order_update_form_ajax'),
	url(r'^order_delete_form_ajax/(?P<pk>\d+)$', views.order_delete_form_ajax, name='order_delete_form_ajax'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
