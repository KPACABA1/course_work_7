from rest_framework.serializers import ModelSerializer

from users.models import User


class UserCreateSerializer(ModelSerializer):
    """Сериализатор для создания моделей пользователей."""
    class Meta:
        model = User
        fields = ('email', 'tg_nick', 'password')


class UserSerializer(ModelSerializer):
    """Сериализатор для моделей пользователей, кроме создания."""
    class Meta:
        model = User
        fields = ('id', 'email', 'tg_nick')
