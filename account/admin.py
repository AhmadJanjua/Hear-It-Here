from django.contrib import admin
from .models import CustomUser, Profile

# allow the admin to update users
admin.site.register(CustomUser)
admin.site.register(Profile)
