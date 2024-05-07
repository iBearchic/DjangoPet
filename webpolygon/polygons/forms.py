from django.contrib.gis import forms as geoforms
from .models import Polygon

class PolygonForm(geoforms.ModelForm):
    class Meta:
        model = Polygon
        fields = ['name', 'polygon', 'crosses_antimeridian']
        widgets = {
            'polygon': geoforms.OSMWidget(attrs={'map_width': 800, 'map_height': 500})
        }