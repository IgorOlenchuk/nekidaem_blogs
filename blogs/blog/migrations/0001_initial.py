# Generated by Django 4.0.4 on 2022-05-16 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=140, verbose_name='Текст')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='ReadPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Прочитал пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Прочитанный пост',
                'verbose_name_plural': 'Прочитанные посты',
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_blog', to=settings.AUTH_USER_MODEL, verbose_name='Чей блог')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь подписан на блог автора',
                'verbose_name_plural': 'Пользователи подписаны на блоги авторов',
                'unique_together': {('user', 'author_blog')},
            },
        ),
    ]
