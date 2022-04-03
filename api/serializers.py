from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    faction_name = serializers.CharField(source='faction.name')
    class Meta:
        model =Character
        fields = ('id', 'name', 'faction_name', 'birth_year', 'birth_planet')
