from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<post_pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^userpage/$', views.userpage, name = 'userpage'),
    url(r'^userlist/$', views.userlist, name = 'userlist'),
    url(r'^userfollow/(?P<username>\w+)/$', views.user_follow, name = 'user_follow'),
    url(r'^following/$', views.following, name = 'following'),
    url(r'^userhome/$', views.user_home, name = 'user_home'),
    url(r'^userposts/$', views.user_posts, name = 'user_posts'),
    url(r'^writepost/$', views.write_post, name = 'write_post'),
    url(r'^delete_post/(?P<post_pk>[0-9]+)/$', views.delete_post, name = 'delete_post'),
    url(r'^comment/(?P<post_pk>[0-9]+)/$', views.comment, name = 'comment'),
    url(r'^export_xlsx/$', views.export_xlsx, name = 'export_xlsx'),
]
