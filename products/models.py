from django.db import models

# Create your models here.
class products_model(models.Model):
    PID = models.IntegerField()
    name = models.CharField(max_length=255)
    tags = models.CharField(max_length=5100)

    def __str__(self):
        return self.title