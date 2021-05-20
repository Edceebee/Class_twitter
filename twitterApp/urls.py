from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='post_list'),
    path('home/<int:pk>/', views.home, name='home'),
    path('home/new/', views.home, name='home'),


]
