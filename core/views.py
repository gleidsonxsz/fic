from django.shortcuts import render
from .models import Area, Publico, Curso

def inicial(request):
    return render(request, 'index.html')

def areas(request):
    lista_areas = Area.objects.all()
    context = {
        'lista_areas': lista_areas
    }
    return render(request, 'areas.html', context)

# Create your views here.
