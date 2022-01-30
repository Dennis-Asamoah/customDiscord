from django.urls import path
#from customDiscord.discord.base.api.views import viewEndpoints
from . import  views



urlpatterns = [path('',views.viewEndpoints),
               path('getUsers/',views.getUsers),
               path('getUser/<str:pk>/',views.getUser),
               path('createUser/',views.createUser),
               path('updateUser/<str:pk>',views.updateUser),
               path('deleteUser/<str:pk>',views.deleteUser),


]