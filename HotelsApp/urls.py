from django.urls import path

from HotelsApp import views

urlpatterns = [
    path('', views.HotelsApp, name='HotelsApp'),
]
