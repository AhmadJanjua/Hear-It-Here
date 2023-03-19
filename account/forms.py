from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'birthday')
