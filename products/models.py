from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.
class products_model(models.Model):
    PID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    tags = models.CharField(max_length=5100)
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def getName(self):
        return self.name

class userHistory(models.Model):
    product = models.ForeignKey(products_model, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.product.name