from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegistrarionView.as_view()),
    path('activation/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
]