# nekidaem_blogs
## Тестовое задание backend #1 (rest api)
[![nekidaem](https://github.com/igorolenchuk/nekidaem_blogs/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master)](https://github.com/IgorOlenchuk/nekidaem_blogs/actions/workflows/main.yml)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

# Index
  - [Описание](#описание)
  - [Главная страница](#главная-страница)
  - [Подписка на авторов](#подписка-на-авторов)
  - [Регистрация и авторизация](#регистрация-и-авторизация)
  - [Полный текст задания](#полный-текст-задания)
  - [Локальное использование](#локальное-использование)
  - [Deploy](#deploy)

<br><br>
**[⬆ Back to Index](#index)**
## Описание
**nekidaem_blog** — онлайн-сервис, где пользователи смогут публиковать посты, 
подписываться на публикации других пользователей.
<br><br>
**[⬆ Back to Index](#index)**
### Главная страница
Содержимое главной страницы — список постов авторов, на которые подписан пользователь, 
отсортированных по дате публикации (от новых к старым).<br>
Пост в блоге — элементарная запись с заголовком, текстом (140 символов) и временем создания.
У пользователя есть персональная лента новостей (не более ~500 постов), в которой выводятся посты из блогов, на которые он подписан, в порядке добавления постов. Пагинация по 10 постов.<br>
Пользователь может помечать посты в ленте прочитанными.<br>
При удалении/добавлении поста, лента тоже изменяется. <br>
<br><br>
**[⬆ Back to Index](#index)**
### Подписка на авторов
Пользователь может подписываться/отписываться на блоги других пользователей (любое количество).<br>
Подписка на публикации доступна только авторизованному пользователю. 
Страница подписок доступна только владельцу.
<br><br>
**[⬆ Back to Index](#index)**
### Регистрация и авторизация
Имеется база пользователей (добавляются через админку/swagger, регистрацию делать не надо). <br>
<br><br>
**[⬆ Back to Index](#index)**
### Полный текст задания
_Реализовать rest api:_
Имеется база пользователей (добавляются через админку/swagger, регистрацию делать не надо). <br>
У каждого пользователя при создании создается персональный блог. Новые создавать он не может. <br>
Пост в блоге — элементарная запись с заголовком, текстом (140 символов) и временем создания.<br>
Заголовок обязательное поле.<br>
Пользователь может подписываться/отписываться на блоги других пользователей (любое количество).<br>
У пользователя есть персональная лента новостей (не более ~500 постов), в которой выводятся посты из блогов, на которые он подписан, в порядке добавления постов. Пагинация по 10 постов.<br>
Пользователь может помечать посты в ленте прочитанными.<br>
При удалении/добавлении поста, лента тоже должна изменяться. <br>
Раз в сутки на почту прилетает подборка из 5 последних постов ленты (можно в консоль).<br>
В среднем пользователь подписан на 100 человек, которые постят по 2-3 раза в день.<br>
Предполагаемое кол-во пользователей в системе около 1 млн.<br>
Будет плюсом, если добавить дамп с большим кол-вом записей или добавить команду, которая сама генерирует большой объем данных.<br>
Можно использовать https://mixer.readthedocs.io/en/latest/api.html https://stackoverflow.com/questions/36463134/generate-test-data-in-postgresql-table <br>
Будет плюсом наличие тестов.<br>

*Требования:*<br>
- Python 3.x (текущая версия 3.9); <br>
- Django > 3.х + Drf (текущая версия 4.04) или FastApi, Postgresql; <br>
- Можно использовать Celery и Redis.<br> 

```Проект должен быть на гитхабе и отражать процесс разработки. НЕ один коммит на всё.
Код максимально приближенный к боевому (насколько получится).
Проект необходимо упаковать в докер. Запускать через docker-compose.
В проекте должно быть README с описанием запуска проекта.
Срок выполнения 1-2 дня.
Ссылку на гитхаб отправить на info@nekidaem.ru.
```
<br><br>
**[⬆ Back to Index](#index)**
## Локальное использование

####1) Создаем `.env` и заполняем переменные окружения, например:

```shell
vim .env
```
```text
SECRET_KEY="bw&*hlrr^p$8qs^@kcvo8@r8sks+@ojtel8j04-t#&@pxl%#o="
DEBUG=True/False
DJANGO_ALLOWED_HOSTS="0.0.0.0, [::1]"
DEFAULT_FROM_EMAIL=example@example.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
###2) Устанавливаем [Docker](https://docs.docker.com/engine/install/)
###3) Собираем `docker-compose` в detach mode (background):
```shell
docker-compose up --build -d --force-recreate
```
###4) Собираем статические файлы в `STATIC_ROOT`:
```shell
docker-compose exec web python3 manage.py collectstatic --noinput
```
###5) Запускаем миграции:
```shell
docker-compose exec web python3 manage.py migrate --noinput
```
###6) Наполняем `Postgres` данными:
```shell
docker-compose exec web python3 manage.py loaddata fixture.json
```
###7) Останавливаем и удаляем контейнеры, сети, тома и образы:
```shell
docker-compose down -v --remove-orphans
```
<br><br>
**[⬆ Back to Index](#index)**
## Deploy
###1) Выдать права на запуск данных скриптов: 
```shell
chmod +x ./blog/entrypoint.sh && chmod +x ./blog/entrypoint.prod.sh
```
###2) Создать образ и запустить контейнер в фоне:
```shell
docker-compose -f docker-compose.yml up -d --build
```
###3) Выполнить миграции
```shell
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
```
###4) Сборка стандартных и подготовленных статических файлов 
```shell
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```
###5) Заполнить таблицы подготовленными данными. `3-4` можно пропустить - сразу запустить этот пункт
```shell
docker-compose -f docker-compose.yml exec web python manage.py fill_db```

### Автор
Игорь Оленчук