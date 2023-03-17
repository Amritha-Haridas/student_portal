from django.urls import path
from . import views

urlpatterns = [
    path('viewlogin/',views.viewlogin,name='viewlogin'),

 
 
]