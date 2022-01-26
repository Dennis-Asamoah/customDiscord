from dataclasses import fields
from django.forms import ModelForm
from .models import  Usersdb,User
from django.contrib.auth.forms import  UserCreationForm

class  UserForm(ModelForm):
    class  Meta:
       model=Usersdb
       fields='__all__' # if u want specify the field put thr field in a list eg [name]  will only display name field  

         
class  RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password1','password2']
     #   fields='__all__'

