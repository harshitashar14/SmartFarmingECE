from django.db import models

# Create your models here.

from django.db import models

class StatusItem(models.Model):
    last_updated = models.TimeField(auto_now=True)
    Temp = models.FloatField(default =1)
    Humidity = models.FloatField(default =1)
    Moisture = models.FloatField(default =1)
    Is_sprinkler_on =  models.IntegerField(default =1)
    Crop_type = models.IntegerField(default =1)
    Optimal_temp = models.FloatField(default =1)
    Optimal_moisture =  models.FloatField(default =1)
    Optimal_humidity =  models.FloatField(default =1)