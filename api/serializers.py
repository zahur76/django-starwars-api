from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    # faction = serializers.ReadOnlyField(source='faction.name')
    class Meta:
        model =Character
        fields = ('id', 'name', 'gender', 'faction', 'birth_year', 'birth_planet')
