from sys import path_hooks
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('app_celebration_mode.urls')),
]