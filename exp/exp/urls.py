"""exp URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from . import services

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^item_detail/',services.item_detail,name="item_detail"),
    url(r'^home_list/',services.home_list,name="home_list"),
    url(r'^most_recent/',csrf_exempt(services.most_recent),name="recent_shoes"),
    url(r'^create_user/',csrf_exempt(services.create_user),name="create_user"),
    url(r'^create_shoe/',csrf_exempt(services.create_shoe),name="create_shoe"),

]
