from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('upload/', UploadImagesView),
    path('gallery/', GetImagesView, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
