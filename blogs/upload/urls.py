from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import UploadFile

urlpatterns = [
    path('', UploadFile.as_view(), name='upload'),
]

if bool(settings.DEBUG):
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
