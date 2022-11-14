from django.db import models

# Create your models here.
class Quote(models.Model):
    part_number = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='N/A')
    compel_price = models.CharField(default='N/A', null=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)

