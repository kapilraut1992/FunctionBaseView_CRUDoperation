from django.urls import path
from .views import registerview,loginview,logoutview

urlpatterns=[
    path('register/',registerview,name='registerpage'),
    path('login/',loginview,name='loginpage'),
    path('logout/',logoutview,name='logoutpage'),
]