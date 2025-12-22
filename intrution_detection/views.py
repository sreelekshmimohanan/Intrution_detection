from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
'''from ML import test
import os
from tensorflow.keras import backend as K

'''
def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')



def reg(request):
    return render(request,'register.html')

def addreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone_number')
        email=request.POST.get('email')
        password=request.POST.get('password')
         
        sa=user(name=name,phone_number=phone,email=email,password=password)
        sa.save()

    return render(request,'index.html',{'message':"Successfully Registered"})

def v_register(request):
    users=user.objects.all()
    return render(request,'v_register.html',{'result':users})

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=='admin@gmail.com' and password=='admin':
        request.session['details']='admin'
        return render(request,'index.html')
    elif user.objects.filter(email=email,password=password).exists():
        userdetails=user.objects.get(email=email,password=password)
        request.session['uid']=userdetails.id
        request.session['uname']=userdetails.name
        return render(request,'index.html')
    else:
        return render(request,'login.html')

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def fedback(request):
    return render(request,'feedback.html')

def addfedbk(request):
    if request.method=="POST":
        a= request.session['uname']
        b=request.POST.get('feedbacks')

        s=feedback(username=a,feedbacks=b)
        s.save()
        return render(request,'feedback.html',{'message':"Thank you for your feedback"})
    
def v_feedback(request):
     e=feedback.objects.all()
     return render(request,'view_feedback.html',{'result':e})

def file(request):
    return render(request,'upload.html')

def addfile(request):
    if request.method=="POST":
        user_name=request.session['uname']
        file=request.FILES['file']
       
        fs = FileSystemStorage()
        file1 = fs.save(file.name,file)
       

        #result = test.predict()
        cus=fileupload(username=user_name,file=file1)
        cus.save()
    return render(request,'upload.html')
    
def v_addfile(request):
    v=fileupload.objects.all()
    return render(request,'view_file.html',{'result':v})

def v_addfile_user(request):
    us=request.session['uname']
    v=fileupload.objects.filter(username=us)
    return render(request,'viewuserfile.html',{'result':v})




