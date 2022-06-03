from .models import Account
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['firstname', 'email', 'phone','messages']

        widgets = {
            "firstname": TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'name': 'name',

                'pattern': '^([A-ZА-Я][a-zа-я]{3,11})$'
            }),

            "email": EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'name': 'email',

                'pattern': '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'name': 'phone',
                'pattern': '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
            }),
            "messages": TextInput(attrs={
                'class': 'form-control',
                'id': 'messages',
                'name': 'messages',


            }),
        }


def print_form(self):
    return str(self) + "\n"


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Name',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder': 'Email',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control','placeholder' : 'Password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control','placeholder' : 'Password',}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),

            "email": EmailInput(attrs={
                'class': 'form-control',
                'pattern': '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
                'placeholder': 'Email',
            }),

            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Password',
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
            }),
        }
