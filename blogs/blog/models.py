from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    # по условиям задачи не указан размер поля названия постов, сделал 39
    title = models.CharField(verbose_name='Заголовок', max_length=30, null=False)
    text = models.TextField(verbose_name='Текст', max_length=140)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    # добавил время обновления постов
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Автор - {self.user} | ' \
               f'Заголовок - {self.title[:15]} | ' \
               f'Текст - {self.text[:30]}...'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        # ранжирование постов по времени добавления/обновления
        ordering = ['-updated']


#Подписка на потсы
class Follow(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE
    )
    author_blog = models.ForeignKey(
        User, verbose_name='Чей блог',
        on_delete=models.CASCADE, related_name='author_blog'
    )

    def __str__(self):
        return f'Пользователь - {self.user} | ' \
               f'Подписан на блог пользователя - {self.author_blog}. '

    class Meta:
        verbose_name = 'Пользователь подписан на блог автора'
        verbose_name_plural = 'Пользователи подписаны на блоги авторов'
        unique_together = (('user', 'author_blog'),)


class ReadPost(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, verbose_name='Прочитал пост', on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Пользователь - {self.user} | ' \
               f'Прочитал пост пользователя - {self.post.user} | ' \
               f'Заголовок - {self.post.title} | ' \
               f'Текст - {self.post.text[:15]}...'

    class Meta:
        verbose_name = 'Прочитанный пост'
        verbose_name_plural = 'Прочитанные посты'
        unique_together = (('user', 'post'),)
