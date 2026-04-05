
from django.contrib import admin

from .models import Answer, Dialog, Message


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'created_at')
    list_filter = ('user', )
    ordering = ('created_at', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'dialog')
    list_filter = ('dialog', )
    ordering = ('created_at', )
    search_fields = ('text', )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'message')
    list_filter = ('message', )
    ordering = ('created_at', )
    search_fields = ('text', )
