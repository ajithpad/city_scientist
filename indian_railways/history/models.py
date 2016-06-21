from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Events(models.Model):
	place = models.CharField(max_length = 100)
	year = models.CharField(max_length = 4)
	picture =  models.FileField()

	def __str__(self):
		return self.place +' in '+ self.year

class Stories(models.Model):
	event = models.ForeignKey(Events, on_delete =  models.CASCADE)
	genre = models.CharField(max_length = 100)
	importance = models.CharField(max_length = 100, default = 'important')
	is_favorite = models.BooleanField(default = False)


	def __str__(self):
		return self.event.place + ' is a ' + self.genre + ' story.'


