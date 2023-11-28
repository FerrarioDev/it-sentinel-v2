from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth.models import User

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
class UserValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        dnarId = data['dnarId']

        if not str(dnarId).isnumeric():
            return JsonResponse({'dnarid_error':'dnarId should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username = dnarId).exists():
            return JsonResponse({'dnarId_error':'dnarId in use, choose another one'}, status=409)
        


        return JsonResponse({'dnarid_valid': True},)



class LogInView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    

