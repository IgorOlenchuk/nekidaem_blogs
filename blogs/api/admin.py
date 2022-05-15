from django.contrib import admin

from blog.models import Post, Follow, ReadPost


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author_blog')
    autocomplete_fields = ['author_blog']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    autocomplete_fields = ['user']


@admin.register(ReadPost)
class ReadPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    autocomplete_fields = ['user']
