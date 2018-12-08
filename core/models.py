from django.db import models

# Create your models here.
class Planet(models.Model):
	name = models.TextField(max_length=50)
	mass = models.TextField()
	radius = models.TextField()
	period_days = models.TextField()
	surface_temperature = models.TextField()
	discovery_year = models.TextField()
	distance_from_sun = models.TextField()
	status = models.TextField(max_length=150)
	to_display = models.BooleanField(default=True)

	def __str__(self):
		return self.name