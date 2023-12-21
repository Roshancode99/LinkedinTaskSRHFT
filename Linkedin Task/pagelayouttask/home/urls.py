from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name='home' ),
    path('signup/', views.SignUp , name='signup'),
    path('login/', views.Login, name='login')
]
