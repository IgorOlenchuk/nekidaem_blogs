from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

handler400 = 'blogs.views.page_bad_request'
handler404 = 'blogs.views.page_not_found'
handler500 = 'blogs.views.server_error'

urlpatterns = [
    # раздел администратора
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('blog.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include('api.urls')),
    path('upload/', include('upload.urls')),
]
