
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ...models import Plant, PlantImages
from .serializers import PlantImagesSerializer, PlantSerializer, UserSerializer


@api_view(['GET', 'POST'])
def plant_list(request):
    if request.method == 'GET':
        queryset = Plant.objects.all()
        serializer = PlantSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def plant_detail(request, id):
    plant = get_object_or_404(Plant, pk=id)
    if request.method == 'GET':
        serializer = PlantSerializer(plant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PlantSerializer(plant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'DELETE':
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def plant_images(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == 'GET':
        images = PlantImages.objects.filter(plant=plant)
        serializer = PlantImagesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PlantImagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(plant=plant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
