from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password1',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password2'
            })
        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password'
            })
        }
