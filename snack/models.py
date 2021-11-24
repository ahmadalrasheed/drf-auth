from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=64)

    def __str__(self):
        return self.name


