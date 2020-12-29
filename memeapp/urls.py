from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('login',views.loginPage, name='loginPage'),
    path('register',views.registerPage,name='registerPage'),
    path('logout', views.logoutPage , name='logoutPage'),
    path('memes',views.memePage, name='memePage')
]