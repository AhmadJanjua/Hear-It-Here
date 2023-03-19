# forum site URL Configuration
from django.contrib import admin
from django.urls import path, include

# main url configurations
urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('comments/', include('comments.urls')),
]
