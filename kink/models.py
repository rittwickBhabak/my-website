from django.db import models
import datetime

# Create your models here.
class Storage(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Video(models.Model):
    title = models.CharField(max_length=100)
    last_seen = models.FloatField(default=0, null=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    last_seen_at = models.DateTimeField(null=True)
    raw_link = models.URLField(null=True)
    mf_link = models.URLField(null=True)
    description = models.TextField(default='')

    def upate_last_seen_at(self, last_seen):
        self.last_seen = last_seen
        self.last_seen_at = datetime.datetime.now()
        super().save()

    def update_raw_link(self, raw_link):
        self.raw_link = raw_link
        super().save()

    def update_mf_link(self, mf_link):
        self.mf_link = mf_link
        super().save()

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    time = models.FloatField()

    def __str__(self):
        return f"{self.video.title} at ({self.time})"

