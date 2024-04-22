from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditCustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }