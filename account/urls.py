from django.urls import path, include
from . import views


app_name = 'account'

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('auth/login/', views.log_in, name='login'),
    path('auth/logout/', views.log_out, name='logout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]