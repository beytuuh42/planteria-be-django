from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class PlantImages(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"Image path for {self.plant.name}"