from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Supers
from .serializers import SuperSerializer

# Create your views here.

@api_view(['GET'])
def get_all_supers(request):
    if request.method == 'GET':
        superhero = Supers.objects.all()
        serializer = SuperSerializer(superhero, many=True)
        return Response(serializer.data)
