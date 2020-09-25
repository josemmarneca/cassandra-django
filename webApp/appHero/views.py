from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Hero
from .serializers import HeroSerializer



@api_view(['PUT', 'GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def api_new_hero(request):
    if request.method == 'GET':
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        hero = Hero()
        serializer = HeroSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data['email']:
                hero.email = serializer.validated_data['email']
            hero.name = serializer.validated_data['name']
            hero.alias = serializer.validated_data['alias']

            hero.save()
            return Response(
                {'status': 'hero created.'},
                status=status.HTTP_201_CREATED
            )

