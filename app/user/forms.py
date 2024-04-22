from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Roles
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    role = forms.ChoiceField(choices=Roles.choices, label='Роль', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
