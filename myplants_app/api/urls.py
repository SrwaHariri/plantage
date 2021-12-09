from django.urls import path, include
from myplants_app.api.views import Plant, PlantType, Seed
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('plant', Plant, basename='plant'),
router.register('planttype', PlantType, basename='plant-type'),
router.register('seed', Seed, basename='seed')


urlpatterns = [
    path('', include(router.urls)),
]
