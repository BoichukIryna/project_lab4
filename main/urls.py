from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('calculate/<int:age>/', views.calculate, name='calculate'),
]