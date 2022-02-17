from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Supers
from .serializers import SuperSerializer
from rest_framework import status

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