from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Polygon
from .forms import PolygonForm
from .serializers import PolygonSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

def add_polygon(request):
    if request.method == 'POST':
        form = PolygonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add')
    else:
        form = PolygonForm()
    
    return render(request, 'polygons/add_polygon.html', {'form': form})

class PolygonViewSet(viewsets.ModelViewSet):
    # ReadOnlyModelViewSet - только на чтение
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'crosses_antimeridian']
    search_fields = ['name']
