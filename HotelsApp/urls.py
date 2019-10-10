from django.conf.urls import url

# from django.urls import path
from HotelsApp import views

urlpatterns = [
    url(r'^$', views.HotelsApp, name='HotelsApp'),
]

