from django.urls import path, include
from myplants_app.api.views import PlantList, PlantDetail, PlantTypeList,PlantTypeDetail, Seed
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('seed', Seed, basename='seed')


urlpatterns = [
    path('', include(router.urls)),
    
    path('plant/',PlantList.as_view(), name='plant-list'),
    path('plant/<int:pk>', PlantDetail.as_view(), name='plant-detail'),
    
    
    path('planttype/',PlantTypeList.as_view(), name='planttype-list'),
    path('planttype/<int:pk>', PlantTypeDetail.as_view(), name='planttype-detail'),
    
]
