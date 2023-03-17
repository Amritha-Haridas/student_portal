from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('registration/',views.registration,name='registration'),
    path('getDetails/',views.getDetails,name='getDetails'),
    path('login/',views.login,name='login'),
    path('getData/',views.getData,name='getData'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('logout/',views.logout,name='logout')
 
 
]
