from django.contrib import admin
from .models import Story, DirtyTalk


# admin.site.site_header = 'Choti Golop Admin'
# admin.site.site_title = 'Choti Golop Admin Area'
# admin.site.index_title = 'Welcome to the Choti Golop admin area'

admin.site.register(Story)
admin.site.register(DirtyTalk)