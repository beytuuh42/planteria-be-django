from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("email", "name")
    list_filter = ('is_active', 'is_superuser')
