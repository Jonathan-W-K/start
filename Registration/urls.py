from django.urls import path
from . import views
from .views import product_list_view
from django.shortcuts import render, redirect

urlpatterns = [
    path('render/', views.render, name='render'),
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('', views.home, name='myhome'),
    path('courses/', views.courses, name='courses'),
    path('coursedash/', views.coursedash, name='coursedash'),
    path('login/', views.login, name='myloginpage'),
    path('custom_login/', views.login, name='login'),
    path('success/', views.success, name='success'),
    path('dashbase/', views.dashbase, name='dashbase'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_course, name='create_course'),
    path('adduser/', views.adduser, name='addinguser'),
    # path('edituser/', views.edituser, name='edituser'),
    # path('addstudent/', views.addstudent, name='addingstudent'),
    path('editstudent/<int:id>/', views.editstudent, name='editstudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('deletestudent/<int:id>/', views.delstudent, name='confirm_delete'),
    path('product/', views.ProductList, name='Product_list'),  # Adjusted URL pattern
    path('products/', product_list_view, name='product_list'),
]

"""
from django.urls import path
from . import views


urlpatterns = [
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
    path('adduser/', views.adduser, name='addinguser'),
    #path('edituser/', views.edituser, name='edituser'),
    #path('addstudent/', views.addstudent, name='addingstudent'),  # Update the view name here
    path('editstudent/<int:id>/', views.editstudent, name='editstudent'),
    path('updatestudent/<int:id>/', views.updatestudent, name='updatestudent'),
    path('deletestudent/<int:id>/', views.delstudent, name='deletestudent'),
    path('Product/', views.ProductList, name='ProductList')
]
"""
