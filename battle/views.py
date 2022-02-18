from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Battle
from .serializers import BattleSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(['GET', 'POST'])
def get_battle(request):
    if request.method == 'GET':
        battle = Battle.objects.all()
        serializer = BattleSerializer(battle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BattleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def get_battle_id(request, pk):
    battle_id = get_object_or_404(Battle, pk=pk)
    if request.method == 'GET':
        serializer = BattleSerializer(battle_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BattleSerializer(battle_id, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        battle_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

