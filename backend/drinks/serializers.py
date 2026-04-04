
from rest_framework import serializers

from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
        read_only_fields = ('id', )
