from django.db import models

# Create your models here.
class Quote(models.Model):
    part_number = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='N/A')
    compel_price = models.FloatField(default=0.0, null=True)
