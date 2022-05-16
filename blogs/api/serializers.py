from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from blog.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_author(data):
    if data.get('author_blog') == data.get('Пользователь'):
        raise ValidationError('Нельзя подписаться на самого себя')
    return data


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'text', 'updated', 'created', 'user')
        model = Post
        extra_kwargs = {'username': {'required': False},
                        'title': {'required': False},
                        'text': {'required': False},
                        }
