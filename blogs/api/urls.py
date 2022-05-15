from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet
from .views import FollowViewSet
from .views import ReadPostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'postpage', PostViewSet, basename='post-page')
router_v1.register(
    r'subscribe',
    FollowViewSet,
    basename='subscribe',
)
router_v1.register(r'read', ReadPostViewSet, basename='read-post')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
