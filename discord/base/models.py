from re import L
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self) :
        return self.email




    # name=models.CharField(max_length=100,unique=True,null=True)
    # email=models.EmailField(unique=True,null=True)
    

    # USERNAME_FIELD='email'
    # REQUIRED_FIELDS=['username']

    # def __str__(self):
    #     return self.email







class  Usersdb(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    country=models.CharField(max_length=200)
   # pic=models.FileField(null=True,default='214.jpg') 


    def __str__(self):
        return self.name


class  Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    writer=models.ForeignKey(Usersdb,on_delete=models.CASCADE)
    dateCreated=models.DateTimeField(auto_now_add=True)
    dateUpdated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  self.title
