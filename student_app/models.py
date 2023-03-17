from django.db import models

# Create your models here.
class Registerdb(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    faddress=models.TextField()
    laddress=models.TextField()
    password=models.CharField(max_length=10,default='')    

class Loggdb(models.Model):
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10,default='')    