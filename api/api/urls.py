from django.conf.urls import url, include
from rest_framework import routers
from api import views
# from django.contrib import admin

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^customer/', include('customer.urls')),
    url(r'^wallet/', include('wallet.urls')),
    url(r'^shop/', include('shop.urls')),

    url(r'^dashbooard', views.dashboard),
    url(r'^index/', views.index_page),
    # url(r'^', include('customer.urls')),
]
