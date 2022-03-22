import uuid
from rest_framework import serializers
from .models import Prices

class PricesSerializer(serializers.ModelSerializer):
    #id = serializers.UUIDField()

    class Meta:
        model = Prices
        fields = ['id', 'price', 'product', 'unit']

    