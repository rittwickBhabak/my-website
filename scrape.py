import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()

import requests, bs4
story_id = [1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]

from choti_golpo.models import Story
def populate(title, text):
    print(f"Adding {title}")
    Story.objects.create(title= title, text = text)

base_url = 'https://goromgolpo.pythonanywhere.com/'
for id in story_id:
    res = requests.get(f"{base_url}{id}")
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    story = soup.select('#story-text')
    title = soup.select('title')
    populate(title, story)


