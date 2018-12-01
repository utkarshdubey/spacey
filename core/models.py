from django.db import models

# Create your models here.
class Planet(models.Model):
	name = models.TextField()
	mass = models.TextField()
	radius = models.TextField()
	period_days = models.FloatField()
	surface_temperature = models.FloatField()
	discovery_year = models.IntegerField()
	distance_from_sun = models.FloatField()
	status = models.TextField()

	def __str__(self):
		name = self.name