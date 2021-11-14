from django.contrib import admin
from kink.models import Storage, Video, Bookmark

# Register your models here.
admin.site.register(Video)
admin.site.register(Storage)
admin.site.register(Bookmark)