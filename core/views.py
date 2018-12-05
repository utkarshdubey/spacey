from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Planet
import json

def load_planet(file_path):
    reader = csv.DictReader(open(file_path))
    for row in reader:
        planet = Planet(name=row['name'], mass=row['mass'], radius=row['radius'], period_days=row['period_days'], surface_temperature=row['surface_temperature'], discovery_year=row['discovery_year'], distance_from_sun=row['distance_from_sun'], status=row['status'])
        planet.save()
        	
def index(request):
  return render(request, 'index.html')

def get_planets(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        planets = Planet.objects.filter(name__icontains = q )[:20]
        results = []
        for planet in planets:
            planet_json = {}
            planet_json['label'] = planet.name
            planet_json['value'] = planet.name
            results.append(planet_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
