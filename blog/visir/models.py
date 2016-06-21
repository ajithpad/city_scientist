from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Data(models.Model):
	dataname = models.CharField(max_length = 100)
	datatype = models.CharField(max_length = 10)
	datalength = models.IntegerField()
	datadata = models.CharField(max_length = 100000, default = '')

	def __str__(self):
		return self.dataname

