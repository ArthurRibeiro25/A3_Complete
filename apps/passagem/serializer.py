from .models import PassagensClass
from rest_framework import serializers

class PassagensClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassagensClass
        fields = '__all__'