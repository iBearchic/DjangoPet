from django.contrib.gis.db import models

class Polygon(models.Model):
    name = models.CharField(max_length=100)
    polygon = models.PolygonField()
    crosses_antimeridian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
