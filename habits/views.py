from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from habits.models import UsefulHabit
from habits.paginations import UserRetrievePagination
from habits.serializers import UsefulHabitSerializer
from users.permissions import IsOwner


class UsefulHabitPublicListAPIView(ListAPIView):
    """Класс для вывода моделей публичных полезных привычек."""
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitCreateAPIView(CreateAPIView):
    """Класс для создания полезных привычек."""
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer

    def perform_create(self, serializer):
        """Метод для автоматической привязки создающего пользователя к полезной привычке."""
        useful_habit = serializer.save()
        useful_habit.creator = self.request.user
        useful_habit.save()


class UsefulHabitUpdateAPIView(UpdateAPIView):
    """Класс для редактирования полезных привычек, доступ имеет только создатель этой привычки."""
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsOwner,)


class UsefulHabitDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей уроков, доступ имеет только создатель этой привычки."""
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    permission_classes = (IsOwner,)


class UsefulHabitUserListAPIView(ListAPIView):
    """Класс для вывода моделей полезных привычек конкретного пользователя."""
    serializer_class = UsefulHabitSerializer
    paginator = UserRetrievePagination()

    def get_queryset(self):
        """Метод для фильтра полезных привычек по текущему пользователю."""
        queryset = UsefulHabit.objects.filter(creator=self.request.user)
        return queryset
