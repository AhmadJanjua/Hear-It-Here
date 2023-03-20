from django import forms
from .models import Post, Comment


# Form that asks the user for title and description
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ['title', 'description']


# make a form for a comment, it asks for the comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
