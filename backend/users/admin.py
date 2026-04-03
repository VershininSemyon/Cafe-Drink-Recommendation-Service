
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import RegistrationToken, User


@admin.register(RegistrationToken)
class RegistrationTokenAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'token',
        'is_used',
    )

    search_fields = (
        'email',
        'username',
        'token',
    )
    
    list_filter = (
        'email',
        'username',
        'is_used'
    )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name'
    )
    
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'groups'
    )
