from .celery import app as celery_app

# Настройка для celery
__all__ = ('celery_app',)