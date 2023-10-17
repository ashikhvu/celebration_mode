from app_celebration_mode import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
]