from django.urls import path
from . import views

# sets the namespace
app_name = 'homepage'
# directs the urls from root
urlpatterns = [
    path('', views.home_response, name='home'),
]