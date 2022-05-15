from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import PostSerializer
from .serializers import FollowSerializer
from .serializers import ReadPostSerializer
from .permissions import IsAuthorOrAdmin
from blog.models import Post


class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^title',)


class CreateDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateDestroyViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrAdmin)
    lookup_field = 'author'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReadPostViewSet(CreateDestroyViewSet):
    serializer_class = ReadPostSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'post'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
