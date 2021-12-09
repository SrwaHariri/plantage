from rest_framework import serializers
from myplants_app.models import Plant, PlantType, Seed


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = "__all__"


class PlantTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantType
        fields = "__all__"


class SeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantType
        fields = "__all__"
