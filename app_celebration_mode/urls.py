from app_celebration_mode import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('signin_page',views.signin_page,name='signin_page'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('change_event',views.change_event,name='change_event'),
    path('logout_page',views.logout_page,name='logout_page'),
]