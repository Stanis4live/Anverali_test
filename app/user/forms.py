from django import forms
from .models import Roles
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

User = get_user_model()


class CustomSignUpForm(SignupForm):
    email = forms.EmailField(label='Email')
    role = forms.ChoiceField(choices=Roles.choices, label='Роль', required=True)

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user


