from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from habits.models import UsefulHabit
from habits.serializers import UsefulHabitSerializer


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
    """Класс для редактирования полезных привычек."""
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer


class UsefulHabitDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей уроков."""
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
