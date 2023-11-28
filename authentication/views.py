from django.shortcuts import render
from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    

class LogInView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')