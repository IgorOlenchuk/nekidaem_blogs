import os
import json

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from blog.settings import JSON_PATH
from personal_blog.models import UserPost


def load_from_json(file_name: str) -> dict:
    """Загружает данные из json файла, дампа талицы, возвращает словарь"""
    with open(
            os.path.join(JSON_PATH, f'{file_name}.json'),
            encoding='utf-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        self.create_users()
        self.create_posts()

    def create_users(self):
        """Создание супер-юзера, пользователей"""
        self.migrate()
        try:
            if not get_user_model().objects.exists():
                self.migrate()
                get_user_model().objects.create_superuser(
                    username='radif',
                    email='mail@radif.ru',
                    password='qwertytrewq')

                get_user_model().objects.create_user(
                    username='Kolya',
                    email='kolya@blog.local',
                    password='qwertytrewq')

                get_user_model().objects.create_user(
                    username='Alyosha',
                    email='alyosha@blog.local',
                    password='qwertytrewq')

                self.syncdb()
        except Exception as e:
            print(e)
            self.create_users()

    def create_posts(self):
        """ Создание постов
        с привязкой к конкретным пользователям,
        которые были созданы выше, по внешним ключам
        """
        posts = load_from_json('personalblogapp_userpost')
        if not UserPost.objects.exists():
            UserPost.objects.all().delete()
            for post in posts:
                user_name = post['fields']['user']
                _user = get_user_model().objects.get(id=user_name)
                post['fields']['user'] = _user

                new_publication = UserPost(**{'id': post['pk']},
                                           **post['fields'])
                new_publication.save()

            self.reset_sequences()
            self.collect_static()

    @staticmethod
    def migrate():
        os.system('python manage.py migrate --noinput')

    @staticmethod
    def syncdb():
        """Принудительное создания таблиц, для последующего авто-заполнения"""
        os.system('python manage.py migrate --run-syncdb')

    @staticmethod
    def reset_sequences():
        """Сброс последовательностей в базе данных после авто-заполнения т-ц"""
        sequence_sql = connection.ops.sequence_reset_sql(
            no_style(), [UserPost, get_user_model()])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

    @staticmethod
    def collect_static():
        """Сборка стандартных и подготовленных статических файлов"""
        os.system('python manage.py collectstatic --no-input --clear')
