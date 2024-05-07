from django.shortcuts import render, redirect
from .forms import PolygonForm

def add_polygon(request):
    if request.method == 'POST':
        form = PolygonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PolygonForm()
    
    return render(request, 'polygons/add_polygon.html', {'form': form})
