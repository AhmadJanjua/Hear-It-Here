# forum site URL Configuration
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# main url configurations
urlpatterns = [
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('forum/', include('forum.urls')),
]

# code to set up where to load images from
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)