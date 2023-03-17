from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *


# Create your views here.
def home(request):
    data = Registerdb.objects.all()
    return render(request,'viewstudent.html',{'data':data})



def registration(request):
    return render(request,'registration.html')

def getDetails(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        faddress =  request.POST.get('faddress')
        laddress =  request.POST.get('laddress')
        password = request.POST.get('password')
        data = Registerdb(fname=fname,lname=lname,email=email,phone=phone,faddress=faddress,laddress=laddress, password= password)
        data.save()
        return redirect('registration')

def login(request):
    return render(request,'login.html')

def getData(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data=Loggdb(email=email, password=password)
        request.session['email'] = email
        request.session['passwordad'] = password
        data = Loggdb(email=email,password= password)
        data.save()
        return redirect('viewstudent')
    else:
        return render(request, 'login.html')


def viewstudent(request):
    data = Registerdb.objects.all()
    return render(request,'viewstudent.html',{'data':data})

def logout(request):
    del request.session['usernamead']
    del request.session['passwordad']
    return redirect('login')