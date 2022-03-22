import uuid
from rest_framework import serializers
from .models import Units


class UnitsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    #title = serializers.CharField(source='unit.UnitName')

    class Meta:
        model = Units
        fields = ['id', 'UnitName']