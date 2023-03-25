from django.urls import path, include
from . import views

# name the app
app_name = 'account'
# create the path to direct the inputs
urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('profile/', views.to_profile, name='redirect'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/update', views.update_profile, name='update_profile'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]