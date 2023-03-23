from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Model that controls the CustomUser and inherits from the base user manager
class CustomUserManager(BaseUserManager):
    # Create a user with additional attributes while extending the base user
    def create_user(self, email, username, password, birthday, **extra_fields):
        # check for missing fields
        if not email:
            raise ValueError('The email field must be set')
        if not username:
            raise ValueError('The username field must be set')
        # normalize the email inputted before adding to the BaseUser
        email = self.normalize_email(email)
        # lowercase user
        username = username.lower()
        # create the base class
        user = self.model(email=email, username=username, birthday=birthday, **extra_fields)
        # set the password
        user.set_password(password)
        # add the user to the database
        user.save(using=self._db)
        return user

    # Create a moderator class
    def create_moderator(self, email, username, password, birthday, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, username, password, birthday, **extra_fields)

    # create a super user
    def create_superuser(self, email, username, password, birthday=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, birthday, **extra_fields)


# create a custom user that has additional attributes
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # FIELDS
    # have emails, username, birthday, joined
    email = models.EmailField(max_length=255, null=False, unique=True)
    username = models.CharField(max_length=50, null=False, unique=True)
    birthday = models.DateField(null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    # have setting attributes
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    # select the default login field
    USERNAME_FIELD = 'username'
    # identified what is required for in the database
    REQUIRED_FIELDS = ['email', 'birthday']
    # have a user manager field
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(default='Hello, I am new', max_length=100, blank=True)
    image = models.ImageField(default='pfp/default.png', upload_to='account/static/pfp', null=True)

    def __str__(self):
        return self.user.username
