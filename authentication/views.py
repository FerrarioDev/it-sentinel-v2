from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from validate_email import validate_email
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.core.mail import send_mail

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm(initial={'dnarId': '', 'email':''})
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
            
            '''email_subject='Activate your account'
            email_body = 'Test Body'
            email = send_mail(
                        email_subject,
                        email_body,
                        "noreply@semycolon.com",
                        [email],
                        fail_silently=False,
                    )
            email.send(fail_silently=False)
            '''
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



class LoginView(View):
    def get(self, request):
        form = LoginForm(initial={'dnarId': ''})
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            dnar_id = form.cleaned_data['dnarId']
            password = form.cleaned_data['password']
            user = authenticate(request, username=dnar_id, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful. Welcome back!")
                return redirect('index')
            else:
                messages.error(request, "Invalid credentials. Please double-check your DNAR ID and password.")
        else:
            messages.error(request, "Invalid form submission. Please review your input.")

        return render(request, 'authentication/login.html', {'form': form})
    
def logoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
