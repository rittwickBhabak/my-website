from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=300)
    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('restaurants:restaurant-detail', args=[self.pk])
    

    def __str__(self):
        return self.title 
