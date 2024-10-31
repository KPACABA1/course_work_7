from rest_framework.serializers import ModelSerializer

from habits.models import UsefulHabit


class UsefulHabitSerializer(ModelSerializer):
    """Сериализатор для моделей полезных привычек."""
    class Meta:
        model = UsefulHabit
        fields = '__all__'