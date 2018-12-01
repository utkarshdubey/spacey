import csv
from django.shortcuts import render
from core.models import Planet

path = 'oec.csv'
with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Planet.objects.get_or_create(
                name=row[0],
                mass=row[2],
                radius=row[3],
                period_days=row[4],
                surface_temperature=row[11],
                discovery_year=row[14],
                distance_from_sun=row[18],
                status=row[24],
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created