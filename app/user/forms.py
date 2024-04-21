from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
