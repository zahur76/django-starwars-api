from cgitb import lookup
from urllib import request
from webbrowser import get
from django import http
from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework import generics
from .serializers import CharacterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from ipware import get_client_ip

from .models import Character
from django.contrib.auth import authenticate

import json

from api import serializers

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[-1].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR') 
# def check_login(request):
#     if request.method == 'POST':
#         print('zazazaa')
#         if request.user is IsAuthenticated:
#             print(request.user)
#             return JsonResponse({"login_status": True})
#         else:
#             # No backend authenticated the credentials
#             return JsonResponse({"login_status": False})   

class all_characters(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # def get(self, request, *args, **kwargs): 
    #     ip = get_client_ip(request)
    #     return ip


class add_characters(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class characterDetails(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_fields = ('pk', 'name')
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

class characterDetails_Id(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_fields = ('pk')
    def get_object(self):
        queryset = self.get_queryset()
        filter = {"id": self.kwargs["pk"]}
        obj = get_object_or_404(queryset, **filter)
        return obj

class characterCRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_fields = ('pk', 'name')
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj