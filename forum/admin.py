from django.contrib import admin
from .models import Category, Post, Comment

# register the models such that the admin can modify the data
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
