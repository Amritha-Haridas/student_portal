from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from student_app . models import *


# Create your views here.
def viewlogin(request):
    data = Loggdb.objects.all()
    return render(request,'viewlogin.html',{'data':data})
