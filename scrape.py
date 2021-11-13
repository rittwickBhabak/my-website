# 'title'
# 'total_pages'
# 'url'
# 'cover_page_url'
# 'author'
# 'last_accessed_page'

# bs = Book.objects.all()
# data = []

# for b in bs:
#     my_dict = {}
#     my_dict['title'] = b.title
#     my_dict[
# 'total_pages'] = b.total_pages
#     my_dict['url'] = b.url
#     my_dict['cover_page_url'] = b.cover_page_url
#     my_dict['author'] = b.author
#     data.append(my_dict)

# print(my_dict)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()
data = [
    {
        'title': '5 Love Languages', 
        'total_pages': 272, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/5%20Love%20Languages/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/5%20Love%20Languages/1.jpg?raw=true', 
        'author': 'Gary Chapman'
    }, 
    {
        'title': '6 Ways To Eat A Pussy', 
        'total_pages': 43, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/6%20Ways%20To%20Eat%20A%20Pussy/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/6%20Ways%20To%20Eat%20A%20Pussy/1.jpg?raw=true', 
        'author': 'Sonia Borg'
    }, 
    {
        'title': '8 Oral Sex Games for Ultimate Fun and Pleasure', 
        'total_pages': 56, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/8%20Oral%20Sex%20Games%20for%20Ultimate%20Fun%20and%20Pleasure/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/8%20Oral%20Sex%20Games%20for%20Ultimate%20Fun%20and%20Pleasure/1.jpg?raw=true', 
        'author': 'Sonia Borg'
    }, 
    {
        'title': '8 Ways To Make Her Come Orally', 
        'total_pages': 49, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/8%20Ways%20To%20Make%20Her%20Come%20Orally/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/8%20Ways%20To%20Make%20Her%20Come%20Orally/1.jpg?raw=true', 
        'author': 'Sonia Borg'
    }, 
    {
        'title': 'Clitology', 
        'total_pages': 268, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Clitology/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Clitology/1.jpg?raw=true', 
        'author': 'Jordan LaRousse & Samantha Sade'
    }, 
    {
        'title': 'Compound Effect', 
        'total_pages': 195, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Compound%20Effect/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Compound%20Effect/1.jpg?raw=true', 
        'author': 'Darren Hardy'
    }, 
    {
        'title': 'Fifth Shades of Kink', 
        'total_pages': 88, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Fifth%20Shades%20of%20Kink/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Fifth%20Shades%20of%20Kink/1.jpg?raw=true', 
        'author': 'Traistan Taormino'
    }, 
    {
        'title': 'Mahabharat', 
        'total_pages': 720, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Mahabharat/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Mahabharat/1.jpg?raw=true', 
        'author': 'রাজশেখর বসু'
    }, 
    {
        'title': 'Meditation for Beginners', 
        'total_pages': 49, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Meditation%20for%20Beginners/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Meditation%20for%20Beginners/1.jpg?raw=true', 
        'author': 'Sara Elliott Price'
    }, 
    {
        'title': 'The One Thing', 
        'total_pages': 201, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/One%20Thing/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/One%20Thing/1.jpg?raw=true', 
        'author': 'Gary W. Keller & Jay Papasan'
    }, 
    {
        'title': 'Two Knotty Boys - Back of the Ropes', 
        'total_pages': 462, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Two%20Knotty%20Boys/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Two%20Knotty%20Boys/1.jpg?raw=true', 
        'author': None
    }, 
    {
        'title': 'Unlimited Memory', 
        'total_pages': 363, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Unlimited%20Memory/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Unlimited%20Memory/1.jpg?raw=true', 
        'author': 'Kevin Horsley'
    }, 
    {
        'title': 'Way of The Superior Man', 
        'total_pages': 146, 
        'url': 'https://github.com/my-personal-repos/library-books/blob/main/Way%20of%20The%20Superior%20Man/', 
        'cover_page_url': 'https://github.com/my-personal-repos/library-books/blob/main/Way%20of%20The%20Superior%20Man/1.jpg?raw=true', 
        'author': 'David Deida'
    }
]

from library.models import Book

def populate():
    for my_dict in data:
        Book.objects.create(
            title = my_dict['title'],
            total_pages = my_dict['total_pages'],
            url = my_dict['url'],
            cover_page_url = my_dict['cover_page_url'],
            author = my_dict['author']
        )


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')