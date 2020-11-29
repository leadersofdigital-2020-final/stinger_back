from rest_framework import serializers
from .models import Compare


class CompareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compare
        fields = '__all__'
