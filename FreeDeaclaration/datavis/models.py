from django.db import models
from uuid import uuid4

# Create your models here.


def upload_location(instance, filename):
    details_image = filename.split('.')
    filename = str(uuid4()) + '.' + details_image[1]
    path = 'map/{}'.format(filename)
    return path


class Region(models.Model):
    id_region = models.IntegerField(unique=True)
    region = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
