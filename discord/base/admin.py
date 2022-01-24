from django.contrib import admin

# Register your models here.

from .models import Post,Usersdb

admin.site.register(Usersdb)
admin.site.register(Post)
