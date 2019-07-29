from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index.html'),
    url(r'^search/', views.search_users, name='search'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^profile/(?P<username>[0-9]+)$', views.person_profile_page, name='person_profile_page'),
    url(r'^edit/profile$', views.edit_profile, name='edit_profile'),
    url(r'^my_profile/(?P<username>[0-9]+)$', views.my_profile, name='my_profile'),
    url(r'^new/image$', views.new_image, name='new_image'),

]