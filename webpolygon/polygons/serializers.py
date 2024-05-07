from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import GEOSGeometry
from .models import Polygon

class PolygonSerializer(serializers.ModelSerializer):
    def validate_polygon(self, value):
        try:
            # Проверка да валидность полигона
            poly = GEOSGeometry(value)
            if not poly.valid:
                raise serializers.ValidationError("Invalid polygon geometry")
        except (ValueError, GEOSGeometry) as e:
            raise serializers.ValidationError("Invalid geometry: " + str(e))
        return value

    class Meta:
        model = Polygon
        fields = '__all__' # Выбираем все поля модели