from rest_framework import filters, mixins, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import PostSerializer

from blog.models import Post

from blog.views import OnlyLoggedUserMixin


class PostViewSet(OnlyLoggedUserMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Обновлен',)


class PostCreateView(OnlyLoggedUserMixin,
                     ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer_class):
        return serializer_class.save()


class SinglePostView(OnlyLoggedUserMixin,
                     RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
