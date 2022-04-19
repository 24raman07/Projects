# Create your models here.

from django.db import models
  
class User(models.Model):
	name = models.CharField(max_length=100)
	id = models.PositiveIntegerField(primary_key=True)
	def __str__(self):
		return self.name
		
		
class Address(models.Model):
	Street = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	Pincode = models.CharField(max_length=50)
	Country = models.CharField(max_length=50)
	
	def __str__(self):
		return self.State
	
