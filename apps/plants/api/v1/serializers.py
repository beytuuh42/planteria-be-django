from rest_framework import serializers
from ...models import Plant, PlantImages


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'name', 'description']


class PlantImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImages
        fields = ['id', 'path']
