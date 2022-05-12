from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_post, name="new_post"),
    path("follow/", views.follow_index, name="follow_index"),
    # Профайл пользователя
    path('<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),
    path('<str:username>/follow/', views.profile_follow, name='profile_follow'),
    path('<str:username>/unfollow/', views.profile_unfollow, name='profile_unfollow'),
]
