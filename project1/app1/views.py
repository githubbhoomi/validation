from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# from django.contrib.auth import User
from django.contrib.auth import authenticate,logout
# Create your views here.
from django.contrib.auth import login as django_login

def client_details(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        zip=request.POST.get('zip')
        logo=request.FILES['logo']
        print(logo)
        details=clients(client=name,image=logo,address=address,zip=zip)
        details.save()
        print("Record saved Successfully")
        return render(request,'home.html')
    return render(request,'clientinfo.html')

def home(request):
    return render(request,'1home.html')


def generate_doc(request):
    if request.method=='POST':
        cmpname=request.POST.get('name')
        cmp=clients.objects.filter(client=cmpname)
        print(cmp)
        if cmp is None:
            return HttpResponse("This company is invalid")
        else:
            k=request.POST.get('generate',"")
            if 'vmp' in k:
                return HttpResponse('vmp')  
    return HttpResponse('none') 

    
def registration(request):
    
    # if request.method=="POST":
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     pas1=request.POST.get('psw1')
    #     pas2=request.POST.get('psw2')
    #     if pas1!=pas2:
    #         messages.success(request,"Password does not match")
    #         return render(request,'registration.html')
    #     elif clients.objects.filter(username=name).first():
    #         messages.success(request,"email is already taken")
    #         return render(request,'registration.html')
    #     else:
    #             user=clients.objects.filter(username=email).first()
    #             if  user is None:
    #                 user_obj=clients.objects.create_user(username=name,email=email,password=pas1)
    #                 user_obj.first_name=name
    #                 user_obj.save()
    #                 messages.success(request,f"{name} Registered successfully")
    #                 return render(request,'registration.html')
    #             else:
    #                 # user_obj=User.objects.create_user(username=email,email=email,password=pas1,is_super=False)
    #                 # user_obj.first_name=name
    #                 # user_obj.save()
    #                 # profile_obj=profile(user=user_obj,user_image=img)
    #                 # profile_obj.save()
    #                 messages.success(request,f"{name} was already Registered")
    #                 return render(request,'register.html')
    return render(request,'registration.html')
    
def login(request):
    if request.method=="POST":
        # name=request.POST.get('name')
        name=request.POST.get('name')
        password=request.POST.get('password')
        print(name,password)
        # user_obj=User.objects.get(email=mail)
        # print(user_obj)
        user=authenticate(username=name,password=password)
        print(user)
        if user is not None:
            print(user,"hi","super")
            django_login(request,user)
            return render(request,'template.html')
        else:
            print("out")
            return render(request,'login.html')
    return render(request,'login.html')
    