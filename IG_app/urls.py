from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index.html'),
    url(r'^search/', views.search_users, name='search'),
    url(r'^new/image$', views.new_image, name='new_image'),
]