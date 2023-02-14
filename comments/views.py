from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def CommentResponse(request) :
    return HttpResponse('This is the Comments Section')