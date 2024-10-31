from rest_framework.generics import CreateAPIView, RetrieveAPIView

from users.models import User
from users.serializers import UserCreateSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Класс для создания моделей пользователей."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        """Вмешиваюсь в логику контроллера для его правильной регистрации пользователей."""
        # Сохраняю пользователя и сразу делаю его активным
        user = serializer.save(is_active=True)

        # Хэширую пароль пользователя и сохраняю пользователя
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    """Класс для просмотра детальной информации об отдельном пользователе."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
