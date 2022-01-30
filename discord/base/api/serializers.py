from  base import  models 
from rest_framework import serializers


class UsersdbSerializer(serializers.ModelSerializer):
     class Meta:
        model=models.Usersdb
        fields='__all__'