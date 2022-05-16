from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, SinglePostView
from .views import PostCreateView


router_v1 = DefaultRouter()
router_v1.register(r'postpage', PostViewSet, basename='post-page')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/post/', PostCreateView.as_view()),
    path('v1/post/<int:pk>', SinglePostView.as_view()),
]
