"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import views

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', csrf_exempt(views.home), name='home'),
    url(r'^shoe_detail', csrf_exempt(views.show_shoe), name='show_shoes'),
    url(r'^user_detail', csrf_exempt(views.show_user), name='show_shoes'),
    url(r'^create_user/', csrf_exempt(views.create_user), name='create_user'),
    url(r'^create_shoe/', csrf_exempt(views.create_shoe), name='create_shoe'),
    url(r'^login',  csrf_exempt(views.login), name='login'),
    url(r'^logout',  csrf_exempt(views.logout), name='logout'),
    url(r'^search',  csrf_exempt(views.search), name='search'),

]
