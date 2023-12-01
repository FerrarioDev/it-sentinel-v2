from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    dnarId = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
