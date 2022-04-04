from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    faction_name = serializers.ReadOnlyField(source='faction.name')
    class Meta:
        model =Character
        fields = ('id', 'name', 'gender', 'faction_name', 'birth_year', 'birth_planet')
