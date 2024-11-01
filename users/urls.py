from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Урылы для пользователей
    path('register/', UserCreateAPIView.as_view(), name='register'),

    # Урлы для ACCESS и REFRESH токенов
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
