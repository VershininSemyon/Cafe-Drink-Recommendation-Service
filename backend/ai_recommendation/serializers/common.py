
from rest_framework import serializers
from ..models import Dialog, Message, Answer


class DialogSerializer(serializers.ModelSerializer):
    message_count = serializers.SerializerMethodField(method_name='get_message_count')

    def get_message_count(self, obj):
        return obj.messages.count()

    class Meta:
        model = Dialog
        fields = '__all__'
        read_only_fields = ('id', 'user')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('id', )
