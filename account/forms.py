from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile


# a form to ask for user information regarding
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, label='Email Address', widget=forms.EmailInput(attrs={'autofocus': True}))
    username = forms.CharField(max_length=50, label='Username')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': True})
        self.fields['username'].widget.attrs.update({'autofocus': False})


# form to update the profile information
class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'bio', 'image')


