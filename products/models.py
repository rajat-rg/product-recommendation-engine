from django.db import models

# Create your models here.
class products_model(models.Model):
    PID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    tags = models.CharField(max_length=5100)
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name