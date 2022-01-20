from django.shortcuts import render
from django.http import HttpResponse


lists=[
    {'id':1,'name':'Dennis'},
    {'id':2,'name':'obide'},
]


def home(request):
    #return  HttpResponse('hello guys')
    context={'list':lists}
    #print('here')
    return render(request,'home.html',context)

def rooms(request,pk):
    context={'pk':pk}
    return render(request,'home.html',context)
    # return HttpResponse('here are rooms')  

def test(request):
    return render(request,'base/new.html')