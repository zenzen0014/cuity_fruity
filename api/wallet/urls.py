# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from wallet import views as v



# urlpatterns = [
#     # url(r'^list/$', v.delivery_list),
#     # url(r'^detail/(?P<pk>[0-9]+)/$', v.delivery_detail),
#     url(r'^$', v.Home, name='home'),

#     url(r'^person/$', v.ViewPerson, name='person_detail'),
#     url(r'^person/add$', v.NewPerson, name='person_add'),
#     url(r'^person/lists/$', v.PeopleList, name='people_list'),
#     url(r'^person/update/$', v.EditPerson, name='person_update'),
#     url(r'^person/delete/$', v.KillPerson, name='person_delete'),


#     url(r'^category/$', v.ViewCategory, name='category_detail'),
#     url(r'^NewCategory$', v.NewCategory, name='category_add'),
#     url(r'^category/lists/$', v.CategoryList, name='category_list'),
#     url(r'^category/update/$', v.EditCategory, name='category_update'),
#     url(r'^category/delete/$', v.DeleteCategory, name='category_delete'),
#     url(r'^category/alternate/$', v.CategoryDetail, name='category_detail_alt'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


from django.conf.urls import patterns, url, include
from wallet.views import *

person_urls = patterns('',
    url(r'^$', ViewPerson.as_view(), name='person_detail'),
    url(r'^update$', EditPerson.as_view(), name='person_update'),
    url(r'^delete$', KillPerson.as_view(), name='person_delete'),
)

category_urls = patterns('',
    url(r'^$', ViewCategory.as_view(), name='category_detail'),
    url(r'^alternate$', CategoryDetail.as_view(), name='category_detail_alt'),
    url(r'^update$', EditCategory.as_view(), name='category_update'),
    url(r'^delete$', DeleteCategory.as_view(), name='category_delete'),
)

urlpatterns = patterns('',
    url(r'^peoples$', PeopleList.as_view(), name='people_list'),
    url(r'^(?P<slug>[\w-]+).person/', include(person_urls)),
    url(r'^newperson$', NewPerson.as_view(), name='person_add'),
    url(r'^categories$', CategoryList.as_view(), name='category_list'),
    url(r'^(?P<slug>[\w-]+).cat/', include(category_urls)),
    url(r'^newcategory$', NewCategory.as_view(), name='category_add'),
)