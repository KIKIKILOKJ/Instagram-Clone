from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^user/(?P<username>\w+)',views.profile,name='profile'),
    url(r'^postImage/',views.post_image,name='postImage'),
    url(r'^user/account/edit/',views.edit_profile,name='editProfile'),
    url(r'^image/(?P<image_id>\d+)',views.view_single_image,name='singleImage'),
    url(r'^search/',views.search,name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)