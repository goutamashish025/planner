from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blogs', views.blogs, name='blogs'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    
]
