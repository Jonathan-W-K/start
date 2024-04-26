"""
URL configuration for start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from Registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('', views.home, name='myhome'),
    path('courses/', views.courses, name='courses'),
    path('coursedash/', views.coursedash, name='coursedash'),
    path('login/', views.login, name='myloginpage'),  # Update the view name here
    path('login/', views.login, name='login'),  # Update the view name here
    path('success/', views.success, name='success'),
    path('dashbase/', views.dashbase, name='dashbase'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_course, name='create_course'),
    path('adduser/', views.adduser, name='addinguser'),  # Update the view name here
    path('addstudent/', views.addstudent, name='addinguser'),  # Update the view name here
    path('editstudent/<int:id>/', views.editstudent, name='editstudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('deletestudent/<int:id>/', views.delstudent, name='deletestudent')
]
