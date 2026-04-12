
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Message
from ..permissions import IsDialogCreator
from ..serializers.common import MessageSerializer
from ..serializers.detailed import DetailedMessageSerializer


class BaseMessageAPIView:
    queryset = Message.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsDialogCreator]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(dialog__user=self.request.user)


class ListCreateMessageAPIView(BaseMessageAPIView, generics.ListCreateAPIView):
    serializer_class = MessageSerializer


class RetrieveDestroyMessageAPIView(BaseMessageAPIView, generics.RetrieveDestroyAPIView):
    serializer_class = DetailedMessageSerializer
