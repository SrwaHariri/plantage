from django.contrib import admin
from myplants_app.models import Plant, PlantType, Seed


# Register your models here.
admin.site.register(Plant)
admin.site.register(PlantType)
admin.site.register(Seed)
