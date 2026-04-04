from django.db import models

# Create your models here.
#DB table for stock card
class stockCard(models.Model):
    name = models.CharField(max_length=100)
    measurement_unit = models.CharField(max_length=50)
    opening_stock = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    current_stock = models.BigIntegerField()