from django.contrib import admin
from .models import Story, DirtyTalk


admin.site.site_header = 'I am Rittwick'
admin.site.site_title = 'I am Rittwick'
admin.site.index_title = 'Welcome to I am Rittwick'

admin.site.register(Story)
admin.site.register(DirtyTalk)