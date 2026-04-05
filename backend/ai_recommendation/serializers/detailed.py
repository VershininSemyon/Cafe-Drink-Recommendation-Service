
from .common import DialogSerializer, MessageSerializer, AnswerSerializer


class DetailedDialogSerializer(DialogSerializer):
    messages = MessageSerializer(many=True, read_only=True)


class DetailedMessageSerializer(MessageSerializer):
    answer = AnswerSerializer(read_only=True)


class DetailedAnswerSerializer(AnswerSerializer):
    message = MessageSerializer(read_only=True)
