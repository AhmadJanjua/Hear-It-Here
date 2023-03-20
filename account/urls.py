from django.urls import path, include
from . import views


app_name = 'account'

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('profile/', views.to_profile, name='redirect'),
    path('<str:username>/', views.profile, name='profile'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]