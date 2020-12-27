from django.urls import path
from .import views
from .views import *

urlpatterns =[
    path('', views.welcome, name='home'),
    path('user-creation/', views.accountcreation,name='user-creation'),
   
]