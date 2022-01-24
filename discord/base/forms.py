from django.forms import ModelForm
from .models import  Usersdb

class  UserForm(ModelForm):
    class  Meta:
       model=Usersdb
       fields='__all__' # if u want specify the field put thr field in a list eg [name]  will only display name field  

         
    
