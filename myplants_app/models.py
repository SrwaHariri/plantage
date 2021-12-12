from django.db import models


class PlantType(models.Model):
    title = models.CharField(max_length=200)
     
    def __str__(self):
        return self.title
 
    class Meta:
        ordering = ['-id']

class Plant (models.Model):
    name = models.CharField(max_length=200)
    plantSeason = models.CharField(max_length=200)
    neededWater = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    placment = models.CharField(max_length=200)
    planttype = models.ForeignKey(
        PlantType, on_delete=models.CASCADE, related_name="plant")

    def __str__(self):
        return str(self.name)+"|"+self.planttype.title


class Seed(models.Model):
    name = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
