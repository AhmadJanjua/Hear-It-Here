from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]