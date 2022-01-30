
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from base.models import Usersdb
from .serializers import UsersdbSerializer

@api_view(['GET'])
def viewEndpoints(request):
    endpoints=['api/', 
               'api/getUsers/',
                'api/getUser/id',
               'api/deleteUser',
               'api/createUser',
               'api/updateUser',  
        ]
    #endpoints={'1':'2'}    

    return Response(endpoints)



@api_view(['GET'])
def getUsers(request):
     users=Usersdb.objects.all()
     users=UsersdbSerializer(users,many=True)
     return Response(users.data)         


@api_view(['GET'])
def getUser(request,pk):
    pk=int(pk)
    user=Usersdb.objects.get(id=pk)
    print(455)
    serializer=UsersdbSerializer(user,many=False)
    print(256)
    return Response(serializer.data)


@api_view (['POST'])
def createUser(request):
    user=UsersdbSerializer(data=request.data)
    if user.is_valid():
         print(456)
         user.save()
    return Response(user.data)      

@api_view(['POST'])
def updateUser(request,pk):
    user=Usersdb.objects.get(id=pk)
    serializer=UsersdbSerializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)    

         

@api_view(['DELETE'])
def deleteUser(request,pk):
    user=Usersdb.objects.get(id=pk)
    user.delete()
    return Response('delete succesfully')
     
     
         
       




