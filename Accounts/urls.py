from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register),
    path('signin/', views.login),
    path('signout/', views.logout),
]
