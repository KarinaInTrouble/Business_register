"""kirill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from WebApp import views


urlpatterns = [
    path('', views.basic, name="index"),
    re_path(r'^delete/(?P<id>\d+)/$',views.delete),
    re_path(r'^delete_1/(?P<id>\d+)/$',views.delete_1),
    re_path(r'^delete_2/(?P<id>\d+)/$',views.delete_2),
    re_path(r'^delete_3/(?P<id>\d+)/$',views.delete_3),
    path('workers/', views.workers, name="workers"),
    path('workers_1/', views.workers_1, name="workers_1"),
    path('workers_2/', views.workers_2, name="workers_2"),
    path('workers_3/', views.workers_3, name="workers_3"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
