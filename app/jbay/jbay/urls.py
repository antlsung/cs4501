"""jbay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from rest_framework import routers
from . import home, user_api, shoe_api
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "home.index", name='index'),
    url(r'^shoes/', shoe_api.shoe_list, name='shoes'),
    url(r'^users/', user_api.user_list, name='users'),
    url(r'^get_shoes/', shoe_api.get_shoes, name='get_shoes'),
    url(r'^add_shoes/', shoe_api.add_shoes, name='add_shoes'),
    url(r'^update_shoes/', shoe_api.update_shoes, name='update_shoes'),
    url(r'^delete_shoes/', shoe_api.delete_shoes, name='delete_shoes'),
    url(r'^get_users/', user_api.get_users, name='get_users'),
    url(r'^add_users/', user_api.add_users, name='add_users'),
    url(r'^update_users/', user_api.update_users, name='update_users'),
    url(r'^delete_users/', user_api.delete_users, name='delete_users')
]
