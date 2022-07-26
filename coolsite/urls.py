from django.contrib import admin
from django.urls import path
from django.shortcuts import render


from django.urls import path, include
urlpatterns = [
    path('', include('man.urls')),
    path('admin/', admin.site.urls),
    path('',include('manual.urls'))
]

