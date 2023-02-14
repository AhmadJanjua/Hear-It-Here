from django.urls import path
from . import views

urlpatterns = [
    path('preview/', views.CommentResponse)
]