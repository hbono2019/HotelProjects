from django.conf.urls import url
from django.urls import path

from HotelsApp import views
from HotelsApp.views import *

app_name = "HotelsApp"
urlpatterns = [
    url(r'^$', views.index, name='index'),

    path('login_index/', views.login_index, name='login_index'),
    path('about/', views.about, name='about'),
    path('accommodation/', views.accomodation, name='accommodation'),
    path('blog/', views.blog, name='blog'),
    path('blogsingle/', views.blogsingle, name='blogsingle'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('gallery/', views.gallery, name='gallery'),
    url(r'^login/$', CustomLoginView.as_view(), name='CustomLoginView'),
    path('account/user_profile/', views.user_profile, name='user_profile'),
    path('account/logout', views.logout, name='logout'),
    path('account/password_reset/', views.password_reset_form, name='password_reset'),
    path('account/password_reset/done', views.password_reset_confirm, name='password_reset_confirm'),
    path('account/reset/<uidb64>/<token>/', views.password_reset_email, name='password_reset_email'),
    path('account/reset/done/', views.password_reset_done, name='password_reset_done'),
    path('account/password_change', views.password_reset_complete, name='password_change'),
]