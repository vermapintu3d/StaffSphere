from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login, name="loginpage"),
    path('signup/', views.signup, name="signup"),
    path('practice/',views.practice, name='practice')
    ]