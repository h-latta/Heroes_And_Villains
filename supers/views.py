from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Supers
from .serializers import SuperSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def get_all_supers(request):
    if request.method == 'GET':
        superhero = Supers.objects.all()
        serializer = SuperSerializer(superhero, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def get_supers_id(request, pk):
    superhero_id = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(superhero_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(superhero_id, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        superhero_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)