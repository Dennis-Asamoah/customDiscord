from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Post,Usersdb
from  .forms  import   UserForm


lists=[
    {'id':1,'name':'Dennis'},
    {'id':2,'name':'obide'},
]


def home(request):
    users=Usersdb.objects.all()
    posts=Post.objects.all()
    #return  HttpResponse('hello guys')
    context={'lists':lists,'users':users,'posts':posts}
    #print('here')
    return render(request,'home.html',context)

def rooms(request,pk):
    pk=int(pk)
    post=Post.objects.get(id=pk)
    #context={'pk':pk}
    #return render(request,'home.html',context)
    return HttpResponse('<h1>{}</h1>'.format(post.id))
    #return render()  

def test(request):
    return render(request,'base/new.html')


def forms(request):
     
     form=UserForm()
     context={'form':form}
     if request.method == 'POST':
         #print (request.POST)
         User=UserForm(request.POST)
         print('good')
         
         if User.is_valid():
           print('5555555')  
           User.save()
           return redirect('home')

     return render (request,'base/forms.html',context)
       


def update (request,pk):
     pk=int(pk)
     user=Usersdb.objects.get(id=pk)
     form=UserForm(instance=user) #to populate field
     context={'form':form}

     if request.method == 'POST':
         
         updateUser=UserForm(request.POST,instance=user)
         if updateUser.is_valid():
             updateUser.save()
             return redirect ('home') 


     return render (request,'base/forms.html',context)


def delete(request,pk):
    pk=int(pk)
    
    if request.method=='POST':
        user=Usersdb.objects.get(id=pk)
        user.delete()
        #users=Usersdb.objects.all()
        #return  render(request,'base/home.html',{'obj':users})
        return redirect ('home')

    return render(request,'base/delete.html')    







