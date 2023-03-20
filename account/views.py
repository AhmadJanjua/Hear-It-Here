from django.core.mail import EmailMessage
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth import login, logout

from .forms import SignUpForm
from .models import CustomUser, Profile


# defines the signup process
def signup(request):
    # check if the request is POST
    if request.method == 'POST':
        # keep a copy of the signup fill info
        form = SignUpForm(request.POST)
        # make sure there are no errors
        if form.is_valid():
            # create a user object without submitting it to the database
            user = form.save(commit=False)
            # make sure the user object cannot log in unless activated
            user.is_active = False
            # commit the user to the database
            user.save()

            # email verification
            subject = 'Activate your Hear It Here account.'
            # configure the url to be account/activate/<id>/<token>
            activation_url = reverse(
                'account:activate', kwargs={
                    'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user)
                })
            # create the email message using a html file.
            message = render_to_string(
                'email/activation_email.html', {
                    'user': user,
                    'domain': get_current_site(request).domain,
                    'activation_url': activation_url
                })
            # set the email address
            to_email = form.cleaned_data.get('email')
            # send email
            email = EmailMessage(subject, message, to=[to_email])
            email.send()
            # Notify the user to check their email
            return HttpResponse('Please confirm your email address to complete the registration.')
    else:
        # if the form wasn't filled before, make a new empty form.
        form = SignUpForm()
    # Display the form using signup html and form
    return render(request, 'registration/signup.html', {'form': form})


# Using the token and id, activate the account
def activate(request, uidb64, token):
    # try to get a user based on the id value supplied
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    # if there are errors or the user doesn't exist, set user to None
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    # Make sure the token is valid
    if user is not None and default_token_generator.check_token(user, token):
        # activate the user, so they can log in.
        user.is_active = True
        user.save()
        # display the confirmation email
        return render(request, 'email/EmailConfirmation.html')
    else:
        # If the id or token are not valid, show this error message
        return HttpResponse('Activation link is invalid!')


# redirects logins to the profile page
def to_profile(request):
    return redirect('account:profile', request.user.username)


# make a simple view of the user's profile
def profile(request, username):
    pf = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile/profile.html', {'profile': pf})


