from django.http import JsonResponse
from rest_framework import generics
from .serializers import CharacterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Character

import json

class all_characters(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class delete_character(APIView):
    def delete(self, request, name):
        try:
            character = get_object_or_404(Character, name=name)
            character.delete()
            return Response({"Response": f'Character {character.name} deleted'})
        except Exception as e:
            return Response({"Response": f'{e}'})
