from django.db import models
from django.urls import reverse 

class Story(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()
    last_height = models.FloatField(default=0)
    is_read = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('choti_golpo:detail-page', kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title 

class DirtyTalk(models.Model):
    text = models.TextField()
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text 