from django.db import models
from django.urls import reverse 

class Book(models.Model):
    title = models.CharField(max_length=500)
    total_pages = models.PositiveIntegerField()
    url = models.URLField(blank=False, null=False)
    cover_page_url = models.URLField(default='https://github.com/my-personal-repos/library-books/blob/main/cover_photo.jpg?raw=true')
    author = models.CharField(max_length=100, null=True, blank=True)
    last_accessed_page = models.PositiveBigIntegerField(default=1)


    class Meta():
        ordering = ['title']
        
    def get_absolute_url(self):
        return reverse("library:detail", kwargs={"pk": self.pk ,"page_number":self.last_accessed_page})
    
    def update_last_accessed_page(self, page_number):
        self.last_accessed_page = page_number
        self.save()

    def __str__(self):
        return self.title 

