from tkinter.font import names
from django.urls import path
from . import views

urlpatterns = [    
    path('',views.home,name='home'),
    path('rooms/<str:pk>',views.rooms,name='rooms'),
    path('new/',views.test,name='new'),
    path('forms/',views.forms,name='forms'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete')
]