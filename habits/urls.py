from django.urls import path

from habits.apps import HabitsConfig
from habits.views import UsefulHabitPublicListAPIView, UsefulHabitCreateAPIView, UsefulHabitUpdateAPIView, \
    UsefulHabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    # Урлы для уроков
    path('list/', UsefulHabitPublicListAPIView.as_view(), name='Useful_habit-list'),
    path('create/', UsefulHabitCreateAPIView.as_view(), name='useful_habit-create'),
    path('<int:pk>/update/', UsefulHabitUpdateAPIView.as_view(), name='useful_habit-update'),
    path('<int:pk>/destroy/', UsefulHabitDestroyAPIView.as_view(), name='useful_habit-destroy'),
]