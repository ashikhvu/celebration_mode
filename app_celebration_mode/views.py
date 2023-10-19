from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_celebration_mode.models import *

def home(request):
    current_theme = ThemesModel.objects.get(id=1)
    events = EventModel.objects.all()
    return render(request,'app_celebration_mode/home.html',{'events':events,'current_theme':current_theme})

def signin_page(request):
    current_theme = ThemesModel.objects.get(id=1)
    events = EventModel.objects.all()
    return render(request,'app_celebration_mode/signin_page.html',{'events':events,'current_theme':current_theme})

def admin_page(request):
    current_theme = ThemesModel.objects.get(id=1)
    events = EventModel.objects.all()
    return render(request,'app_celebration_mode/admin_page.html',{'events':events,'current_theme':current_theme})

def userlogin(request):
    try:
        if request.method=='POST':
            try:
                username = request.POST.get('signin_username')
                password = request.POST.get('signin_password')
                user_data = auth.authenticate(username=username,password=password)
                if user_data is not None:
                    if user_data.is_superuser==True and user_data.is_staff==True:
                        login(request,user_data)
                        messages.success(request,f'Welcome {username} admin')
                        return redirect('admin_page')
                    # elif user_data.is_superuser==False and user_data.is_staff==True:
                    #     auth.login(request,user_data)
                    #     messages.success(request,f'Welcome Doctor {username} ')
                    #     return redirect('user1_profile',pk=user_data.id)
                    # elif user_data.is_superuser==False and user_data.is_staff==False:
                    #     auth.login(request,user_data)
                    #     messages.success(request,f'Welcome patient {username} ')
                    #     return redirect('user2_profile',pk=user_data.id)
                else:
                    messages.error(request,"Invalid login credentials")
                    return redirect('signin_page')
            except:
                messages.error(request,'Invalid login credentials')
                return redirect('signin_page')
    except:
        messages.error(request,'Invalid login credential')
        return redirect('signin_page')
    return redirect('signin_page')


def change_event(request):
    if request.method=='GET':
        select = request.GET.get('event_mode')
        events = EventModel.objects.get(id=select)
        # print(events.event_name)
        set_theme = ThemesModel.objects.get(id=1)
        set_theme.theme_name = events
        set_theme.save()
        print(f'\n{set_theme.theme_name.id}\n')
    return redirect(admin_page)

def logout_page(request):
    auth.logout(request)
    return redirect(home)