from django.urls import path
from . import views

urlpatterns = [
    # в задании сказано, что регистрация пользователя не обязательно, тем не менее
    path("signup/", views.SignUp.as_view(), name="signup"),
]