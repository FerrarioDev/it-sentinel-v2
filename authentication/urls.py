from django.urls import path
from .views import RegisterView, LogInView, UserValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('validate=id', csrf_exempt(UserValidationView.as_view()), name='validation'),
    path('login/',  LogInView.as_view(), name='login'),
]
