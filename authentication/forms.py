from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='DNAR ID',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )