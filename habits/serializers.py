from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from habits.models import UsefulHabit


class UsefulHabitSerializer(ModelSerializer):
    """Сериализатор для моделей полезных привычек."""
    def validate(self, data):
        """Проверка на то, что при редактировании или создании только одно поле из полей: pleasant_habit или award
        заполнено."""
        if ('pleasant_habit' in data and data['pleasant_habit']) and ('award' in data and data['award']):
            raise serializers.ValidationError({
                'error': 'У вас должно быть заполнено либо поле приятной привычки, либо вознаграждение за выполнение '
                         'полезной привычки'
            })
        return data

    class Meta:
        model = UsefulHabit
        fields = '__all__'