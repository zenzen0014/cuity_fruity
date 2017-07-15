from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import home,test_query,supplier_page,customer_page,delivery_page,weui_page, UserList, UserDetail, MenuList, MenuDetail, WalletList, WalletDetail, OrderList, OrderDetail, LocationList, LocationDetail, TestJoin

urlpatterns = [
    url(r'^$', home),
    url(r'^supplier$', supplier_page),
    url(r'^customer$', customer_page),
    url(r'^delivery$', delivery_page),
    url(r'^weui$', weui_page),
    url(r'^test_query', test_query),


    url(r'^users', UserList.as_view()),
    url(r'^user/([0-9])/$', UserDetail.as_view()),


    url(r'^menus', MenuList.as_view()),
    url(r'^menu/([0-9])/$', MenuDetail.as_view()),


    url(r'^wallets', WalletList.as_view()),
    url(r'^wallet/([0-9])/$', WalletDetail.as_view()),


    url(r'^orders', OrderList.as_view()),
    url(r'^order/([0-9])/$', OrderDetail.as_view()),


    url(r'^locations', LocationList.as_view()),
    url(r'^location/([0-9])/$', LocationDetail.as_view()),


    url(r'^test', TestJoin.as_view()),


]