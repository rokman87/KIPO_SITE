from django import forms
from .models import Siteuser, Applications
from django.forms import ModelForm, TextInput, Select


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Siteuser
        fields = ["firstname", "lastname", "username", "password1", "password2", "email", "phone"]
        widgets = {
            "firstname": forms.TextInput(attrs={'class': 'form-control'}),
            "lastname": forms.TextInput(attrs={'class': 'form-control'}),
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=25,
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=30,
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class ApplicationsForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['name', 'institution_type']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "institution_type": Select(attrs={
                'class': 'form-control',
            }, choices=[
                ('Вуз', 'Вуз'),
                ('Колледж', 'Колледж'),
                ('Школа', 'Школа'),
            ])
        }
