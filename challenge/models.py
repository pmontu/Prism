from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
	title = models.CharField(max_length=200)
	frequency = models.PositiveIntegerField()
	startdate = models.DateField()
	numberofdays = models.PositiveIntegerField()
	challengers = models.ManyToManyField(User)