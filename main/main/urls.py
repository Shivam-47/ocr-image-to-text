from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name="home_page"),
    path('api/',include('api.urls')),
]
