from django.urls import path
from .views import RegisterView, LoginView, UserValidationView, EmailValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('validate-id', csrf_exempt(UserValidationView.as_view()), name='validation_id'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validation_email'),
    path('login/', LoginView.as_view(), name='login'),
]
