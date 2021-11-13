from django import forms
from django.forms import widgets 
from .models import Book 

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'total_pages', 'url', 'author', 'cover_page_url')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'total_pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_page_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
        