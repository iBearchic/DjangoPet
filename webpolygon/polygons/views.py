from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Polygon
from .forms import PolygonForm
from .serializers import PolygonSerializer

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
    # ReadOnlyModelViewSet
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
