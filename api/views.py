from math import factorial
from django.http import JsonResponse
from .serializers import CharacterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from .models import Character, Faction

import  json

# Create your views here
@api_view(["GET"])
def all_characters(request):
    '''
        View to return all Characters
    '''
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        all_characters = Character.objects.all()
        data = CharacterSerializer(all_characters, many=True).data
        return Response(data)

    return Response({"Authorisation": 'denied'})
    
    

@api_view(["POST"])
def add_character(request):
    '''
        View to Add or Update Character
    '''
    if request.method == "POST":
        data = request.data        
        try:
            character = get_object_or_404(Character, name=data['name'])
        except:
            character = None
        if character:
            update_character = CharacterSerializer(instance=character, data=data, partial=True)
            if update_character.is_valid():
                update_character.save()
                return Response({"Response": 'Character Updated'})
            errors = create_character._errors
            return Response({"Error": errors})
        else:
            create_character = CharacterSerializer(data=data)
            if create_character.is_valid():
                create_character.save()
                return Response({"Character Created": data})
            errors = create_character._errors
            return Response({"Error": errors})


@api_view(["DELETE"])
def delete_character(request, name):
    try:
        character = get_object_or_404(Character, name=name)
        character.delete()
        return Response({"Response": f'Character {character.name} deleted'})
    except Exception as e:
        return Response({"Response": f'{e}'})
