from unicodedata import name
from django.db import models

# Create your models here.

class  Usersdb(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    country=models.CharField(max_length=200)

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
