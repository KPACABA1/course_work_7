from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для полезных привычек."""
    list_display = ('id', 'email')