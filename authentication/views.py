from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import json
from .models import CustomUser
from validate_email import validate_email
from django.contrib import messages
from .forms import RegistrationForm
from django.core.mail import send_mail

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'authentication/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            dnarId = form.cleaned_data['dnarId']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if user already exists
            if CustomUser.objects.filter(dnarId=dnarId).exists():
                messages.error(request, 'DNAR ID is already registered.')
                return render(request, 'authentication/register.html', {'form': form})

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
                return render(request, 'authentication/register.html', {'form': form})

            if len(password) < 6:
                messages.error(request, 'Password too short.')
                return render(request, 'authentication/register.html', {'form': form})

            # Create and save the user
            user = CustomUser.objects.create_user(dnarId=dnarId, email=email, password=password)
            user.is_active = False
            user.save()
            email_subject='Activate your account'
            email_body = ''
            email = send_mail(
                        email_subject,
                        email_body,
                        "noreply@semycolon.com",
                        [email],
                        fail_silently=False,
                    )
            messages.success(request, 'Account successfully created.')
            return redirect('login')  # Redirect to the login page after successful registration

        # Form is not valid, re-render the registration page with errors
        return render(request, 'authentication/register.html', {'form': form})
    

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'}, status=400)
        if CustomUser.objects.filter(email = email).exists():
            return JsonResponse({'email_error':'Sorry email is in use, choose another one'}, status=409)

        return JsonResponse({'email_valid': True},)


class UserValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        dnarId = data['dnarId']

        if not str(dnarId).isnumeric():
            return JsonResponse({'dnarid_error':'Dnar ID should only contain numeric characters'}, status=400)
        if CustomUser.objects.filter(dnarId = dnarId).exists():
            return JsonResponse({'dnarId_error':'dnarId in use, choose another one'}, status=409)

        return JsonResponse({'dnarid_valid': True},)



class LogInView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
