from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework import serializers

from blog.models import Post
from blog.models import ReadPost
from blog.models import Follow


def validate_author(data):
    if data.get('author_blog') == data.get('Пользователь'):
        raise ValidationError('Нельзя подписаться на самого себя')
    return data


class PostSerializer(serializers.ModelSerializer):
    author_blog = serializers.CharField(source='user')

    class Meta:
        fields = ('title', 'text', 'updated', 'created', 'author_blog')
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = '__all__'
        model = Follow
        validators = (validate_author, )


class ReadPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ReadPost
