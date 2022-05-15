from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from blog.models import Post
from blog.models import ReadPost
from blog.models import Follow


def validate_author(data):
    if data.get('author_blog') == data.get('Пользователь'):
        raise ValidationError('Нельзя подписаться на самого себя')
    return data


class PostSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post


class FollowSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = '__all__'
        model = Follow
        validators = (validate_author, )


class ReadPostSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReadPost
