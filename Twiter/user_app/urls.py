
from django.urls import path, include
from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('signup/', views.signup, name="signup"),
    path('login_form/', views.login_form, name="login_form"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_form, name="logout"),
]