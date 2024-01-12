# In forms.py
import hashlib

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "رمز دوم با رمز اول برابر نیست.",
        'username_exists': "شماره موبایل یا ایمیل قبلا ثبت شده است.",
        'password_too_short': "رمز عبور باید حداقل 8 کاراکتر داشته باشد.",
        'password_common': "این رمز عبور بسیار رایج است.",
        'password_entirely_numeric': "این رمز عبور کاملاً عددی است.",
        'required': "فیلدهای خالی را پر کنید.",  # Update the message for required fields
    }

    class Meta:
        model = User  # Replace with your actual user model
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['username_exists'],
                code='username_exists',
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        return password2

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError(
                self.error_messages['password_too_short'],
                code='password_too_short',
            )

        return password1

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not username or not password1 or not password2:
            raise forms.ValidationError(
                self.error_messages['required'],
                code='required',
            )

        return cleaned_data
