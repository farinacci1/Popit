from django.urls import path
from django.conf.urls import url
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.home, name='Poppit-index'),
    path('logIn/', views.logIn, name='Poppit-Login'),
    path('Registration/', views.signUp, name='Poppit-SignUp'),
    path('userProfile/', views.profile, name='Poppit-Home'),
    path('logout/', views.logout, name='logout')
]
