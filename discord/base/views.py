from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  .models import Post,Usersdb
from  .forms  import   UserForm,RegisterForm
from  django.db.models import Q



lists=[
    {'id':1,'name':'Dennis'},
    {'id':2,'name':'obide'},
]



def loginUser(request):  ###never name it login
     context={'loging_in':'login'}  
     if request.method=='POST':
           email=request.POST.get('email')
           email.lower()
           password=request.POST.get('password')


           user=authenticate(request,email=email,password=password)
           print (user)
           if user is None:
                messages.error(request,'email or paaword incorrect')
           else:
                print('goood')
                login(request,user)
                print('joooo')
                print(dir(request))
                print(user)
                #return HttpResponse('12')

                return redirect('home')    
                 

           
     return render(request,'base/loginForms.html',context)


def Registration(request):
    form=RegisterForm()
    context={'form':form}
    if request.method=='POST':
       userReg=RegisterForm(request.POST)
       
       if userReg.is_valid():
           userReg.save(commit=False)
           userReg.email=request.POST.get('email').lower()
           userReg.save()
           return redirect('loginuser')
           #return HttpResponse('12')
    return render(request,'base/loginForms.html',context)





@login_required(login_url='loginuser')
def logoutUser(request):
    logout(request)
    return redirect('loginuser') 




@login_required(login_url='loginuser')
def home(request):
    users=Usersdb.objects.all()
    posts=Post.objects.all()
    #return  HttpResponse('hello guys')
    context={'lists':lists,'users':users,'posts':posts}
    print('here')
    return render(request,'home.html',context)

    
@login_required(login_url='loginuser')
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







