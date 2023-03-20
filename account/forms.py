from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# a form to ask for user information regarding
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255)
    username = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'birthday')
