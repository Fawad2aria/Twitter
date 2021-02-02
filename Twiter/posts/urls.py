from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('tweets/', views.tweets, name="tweets"),
    path('create_chirp/', views.create_chirp, name="create_chirp"),
    path('likes/<int:twit_id>', views.likes, name="likes"),
    path('profile/<str:user_name>', views.user_tweet, name="user_tweet"),
  
]