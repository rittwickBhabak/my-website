from typing import Tuple
from django.db import models
from django.urls import reverse

class Chapter(models.Model):
    title = models.CharField(max_length=200, default="Add Title")
    total_pages = models.IntegerField()
    slno = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering = ['slno']

    def get_absolute_url(self):
        return reverse("english_grammar:chapter-list", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title 

class Page(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='pages')
    url = models.URLField(max_length=1000)
    
    def __str__(self):
        return f"{self.chapter.title}: {self.pk}"


