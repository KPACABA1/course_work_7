from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers

from habits.models import UsefulHabit
from habits.validators import validate_time_to_complete


class UsefulHabitSerializer(ModelSerializer):
    """Сериализатор для моделей полезных привычек."""
    # Проверка на то, что поле time_to_complete не больше 120 секунд
    time_to_complete = CharField(validators=[validate_time_to_complete])

    def validate(self, data):
        """Проверка на то, что при редактировании или создании только одно поле из полей: pleasant_habit или award
        заполнено, а так же проверка на то что время на выполнение не больше 120 секунд."""
        if ('pleasant_habit' in data and data['pleasant_habit']) and ('award' in data and data['award']):
            raise serializers.ValidationError({
                'error': 'У вас должно быть заполнено либо поле приятной привычки, либо вознаграждение за выполнение '
                         'полезной привычки'
            })
        return data

    class Meta:
        model = UsefulHabit
        fields = '__all__'