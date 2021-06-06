from django.urls import path

from twitterApp.views import home


urlpatterns = [
    path('', home, name='post_list'),
    path('home/<int:pk>/', home, name='home'),
    path('home/new/', home, name='home'),



]
