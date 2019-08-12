"""Achievegoals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from goals.views import *

if settings.DEBUG:
    urlpatterns = [
    path(r'',index,name='index'),
    path('index', index,name='index'),
    path('abount',about,name='about'),
    path('sell',sell,name='sell'),
    path('sign_in',sign_in,name='sign_in'),
    path('seach', seach, name='seach'),
    path('seachx',seachx,name='seachx'),
    path('seachg', seachg, name='seachg'),
    path('seachz', seachz, name='seachz'),
    path('seachnull', seachnull, name='seachnull'),
    path('register',register,name='register'),
    path('register2', register2, name='register2'),
                      path('productg1', productg1, name='productg1'),
                      path('productg2', productg2, name='productg2'),
                      path('productg3', productg3, name='productg3'),
                      path('productg4', productg4, name='productg4'),
                      path('productg5', productg5, name='productg5'),
                      path('productg6', productg6, name='productg6'),
                      path('productg7', productg7, name='productg7'),
                      path('productx1', productx1, name='productx1'),
                      path('productx2', productx2, name='productx2'),
                      path('productx3', productx3, name='productx3'),
                      path('productx4', productx4, name='productx4'),
                      path('productx5', productx5, name='productx5'),
                      path('productx6', productx6, name='productx6'),
                      path('productz1', productz1, name='productz1'),
                      path('productz2', productz2, name='productz2'),
                      path('productz3', productz3, name='productz3'),
                      path('productz4', productz4, name='productz4'),
                      path('productz5', productz5, name='productz5'),
                      path('productz6', productz6, name='productz6'),
                      path('productz7', productz7, name='productz7'),
    path('admin/', admin.site.urls),
    path('api/',include('goals.urls')),
   ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
else:
    urlpatterns = [
        path(r'', index, name='index'),
        path('index', index, name='index'),
        path('abount', about, name='about'),
        path('sell', sell, name='sell'),
        path('sign_in', sign_in, name='sign_in'),
        path('seach', seach, name='seach'),
        path('seachx', seachx, name='seachx'),
        path('seachg', seachg, name='seachg'),
        path('seachz', seachz, name='seachz'),
        path('seachnull', seachnull, name='seachnull'),
        path('register', register, name='register'),
        path('register2', register2, name='register2'),
        path('productg1', productg1, name='productg1'),
        path('productg2', productg2, name='productg2'),
        path('productg3', productg3, name='productg3'),
        path('productg4', productg4, name='productg4'),
        path('productg5', productg5, name='productg5'),
        path('productg6', productg6, name='productg6'),
        path('productg7', productg7, name='productg7'),
        path('productx1', productx1, name='productx1'),
        path('productx2', productx2, name='productx2'),
        path('productx3', productx3, name='productx3'),
        path('productx4', productx4, name='productx4'),
        path('productx5', productx5, name='productx5'),
        path('productx6', productx6, name='productx6'),
        path('productz1', productz1, name='productz1'),
        path('productz2', productz2, name='productz2'),
        path('productz3', productz3, name='productz3'),
        path('productz4', productz4, name='productz4'),
        path('productz5', productz5, name='productz5'),
        path('productz6', productz6, name='productz6'),
        path('productz7', productz7, name='productz7'),
        path('admin/', admin.site.urls),
        path('api/', include('goals.urls')),
                  ]