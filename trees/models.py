from django.db import models

# Create your models here.
class Tree(models.Model):
    common_name = models.CharField(max_length=30)
    scientific_name = models.CharField(max_length=100)
    fact1 = models.CharField(max_length=100)
    pickup_line = models.CharField(max_length=100)

    def __str__(self):
        return self.common_name