from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Events(models.Model):
	place = models.CharField(max_length = 100)
	year = models.IntegerField()
	picture =  models.CharField(max_length = 1000)

	def __str__(self):
		return self.place +' in '+str(self.year)

class Stories(models.Model):
	event = models.ForeignKey(Events, on_delete =  models.CASCADE)
	genre = models.CharField(max_length = 100)


