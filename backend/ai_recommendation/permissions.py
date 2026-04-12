
from rest_framework import permissions
from .models import Dialog, Message


class IsDialogCreator(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if isinstance(obj, Dialog):
            return obj.user == user
        elif isinstance(obj, Message):
            return obj.dialog.user == user

        return False
