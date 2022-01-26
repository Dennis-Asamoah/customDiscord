from tkinter.font import names
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [    
    path('',views.home,name='home'),
    path('rooms/<str:pk>',views.rooms,name='rooms'),
    path('new/',views.test,name='new'),
    path('forms/',views.forms,name='forms'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('loginuser/',views.loginUser,name='loginuser'),
    path('logoutuser/',views.logoutUser,name='logoutuser'),
    path('registration/',views.Registration,name='registration'),
]