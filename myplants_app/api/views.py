from myplants_app.models import Plant, PlantType, Seed
from myplants_app.api.serializers import PlantSerializer, PlantTypeSerializer, SeedSerializer
from rest_framework import viewsets


class Plant(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantType(viewsets.ModelViewSet):
    queryset = PlantType.objects.all()
    serializer_class = PlantTypeSerializer


class Seed(viewsets.ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
