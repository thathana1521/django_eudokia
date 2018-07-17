from django.db import models

class Room(models.Model):
	name = models.CharField(max_length=150)
	capacity = models.IntegerField()
	building = models.CharField(max_length=150)
	date = models.DateTimeField()
	
	def __str__(self):
		return self.name
	
