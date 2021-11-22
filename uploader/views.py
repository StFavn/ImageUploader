
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UploadImagesView(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    else:
        return Response(status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetImagesView(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)
    