
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Dialog
from ..permissions import IsDialogCreator
from ..serializers.common import DialogSerializer
from ..serializers.detailed import DetailedDialogSerializer


class BaseDialogAPIView:
    queryset = Dialog.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsDialogCreator]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ListCreateDialogAPIView(BaseDialogAPIView, generics.ListCreateAPIView):
    serializer_class = DialogSerializer

    def perform_create(self, serializer):
        data = serializer.save(user=self.request.user)
        return data


class RetrieveDestroyDialogAPIView(BaseDialogAPIView, generics.RetrieveDestroyAPIView):
    serializer_class = DetailedDialogSerializer
