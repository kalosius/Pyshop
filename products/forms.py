from django import forms
from .models import Registration


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'password']

