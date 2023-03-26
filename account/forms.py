from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile


# a form to ask for user information regarding
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, label='Email Address')
    username = forms.CharField(max_length=50, label='Username')

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'birthday')


# form to update the profile information
class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'bio', 'image')


