from rest_framework import serializers

from chat.models import Chat


class ChatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
