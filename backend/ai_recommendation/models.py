
import uuid

from django.db import models
from users.models import User


class Dialog(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, related_name='dialogs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Диалог {self.id} пользователя {self.user.username}"


class Message(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    dialog = models.ForeignKey(Dialog, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    filters = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сообщение {self.text}'


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    message = models.OneToOneField(Message, related_name='answer', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ответ {self.text}'
