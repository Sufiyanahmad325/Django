"""
URL configuration for projectCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name= "home"),
    path('about/' , views.about , name= "about"),
    path('contact/' , views.contact , name= "contact"),
    path('myApp/', include('myApp.urls')), #maine yaha myApp nam k app ko yaha include kiya hai taki uske urls ko bhi access kar sakein 

    #ye tailwind reload urls hai isko nnhi dene pe css reload nhi hoga jab bhi hamara code change hoga to ye url hamare browser ko reload kar dega
    path("__reload__/", include("django_browser_reload.urls")), # yaha pe hamne django_browser_reload ka url include kiya hai taki hamara browser reload ho sakein jab bhi hamara code change ho
]
