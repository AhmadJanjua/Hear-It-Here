# accounts/views.py

from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import SignUpForm
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Email verification
            mail_subject = 'Activate your Hear It Here account.'
            activation_url = reverse('account:activate', kwargs={
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'activation_url': activation_url
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return HttpResponse('Please confirm your email address to complete the registration.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def main(request):
    return HttpResponse("This is the main accounts page!")

def login(request):
    return HttpResponse("This is the login page!")
