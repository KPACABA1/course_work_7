from rest_framework.serializers import ValidationError


def validate_time_to_complete(value):
    if value > 120:
        raise ValidationError('Время на выполнение больше 120 секунд')