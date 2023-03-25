from django.db import models
from account.models import CustomUser


# make category with a unique name
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    content = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


# Model the post object
class Post(models.Model):
    # Fields for the post model
    title = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    # foreign references to user and a category
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Comment model
class Comment(models.Model):
    # field of the model
    description = models.TextField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    # Foreign keys to user and post
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
