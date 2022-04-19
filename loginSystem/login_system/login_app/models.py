from django import forms
from django.db import models

# Create your models here.

class User(models.Model):
    
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)


    class Meta:
        ordering = ['name']

#    def get_absolute_url(self):
#       """Returns the URL to access a particular author instance."""
#       return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
