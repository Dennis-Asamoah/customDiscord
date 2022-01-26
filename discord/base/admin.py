from django.contrib import admin

# Register your models here.

from .models import Post,Usersdb,User

admin.site.register(Usersdb)
admin.site.register(Post)
admin.site.register(User)
