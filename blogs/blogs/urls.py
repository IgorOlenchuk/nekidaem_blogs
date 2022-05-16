from django.contrib import admin
from django.urls import include, path

handler400 = 'blogs.views.page_bad_request'
handler404 = 'blogs.views.page_not_found'
handler500 = 'blogs.views.server_error'

urlpatterns = [
    # раздел администратора
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
]

urlpatterns += [
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    path('upload/', include('upload.urls')),
]
