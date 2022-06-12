from django.contrib.auth.models import User
from django.forms import TextInput
from .models import Profile
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput())


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control btn alert-secondary',
        'placeholder': 'Введите пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control btn alert-secondary',
        'placeholder': 'Повторно введите пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control btn alert-secondary',
                'placeholder': 'Логин',
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control btn alert-secondary',
                'placeholder': 'Имя пользователя',
            }),
            "email": TextInput(attrs={
                'class': 'form-control btn alert-secondary',
                'placeholder': 'Адрес электронной почты'
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')