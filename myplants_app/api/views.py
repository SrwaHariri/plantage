from django.shortcuts import get_object_or_404
from myplants_app.models import Plant, PlantType, Seed
from myplants_app.api.serializers import PlantSerializer, PlantTypeSerializer, SeedSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class PlantList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        plant = Plant.objects.all()
        serializer = PlantSerializer(
            plant, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PlantDetail(APIView):
    
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlantSerializer(
            plant, context={'request': request})
        return Response(serializer.data)
   
    def put(self, request, pk):
        plant = Plant.objects.get(pk=pk)
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plant= Plant.objects.get(pk=pk)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PlantTypeList(APIView):
    
    def get(self, request):
        plantType = PlantType.objects.all()
        serializer = PlantTypeSerializer(
            plantType, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class PlantTypeDetail(APIView):
    
    def get(self, request, pk):
        try:
            plantType = PlantType.objects.get(pk=pk)
        except PlantType.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlantTypeSerializer(
            plantType, context={'request': request})
        return Response(serializer.data)
   
    def put(self, request, pk):
        plantType = PlantType.objects.get(pk=pk)
        serializer = PlantTypeSerializer(plantType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plantType= PlantType.objects.get(pk=pk)
        plantType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Seed(viewsets.ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer


