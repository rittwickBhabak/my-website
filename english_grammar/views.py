from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView
from django.views.generic.edit import CreateView
from .models import Chapter, Page

class ChapterList(ListView):
    model = Chapter 

class ChapterDetail(DetailView):
    model = Chapter 

class UpdateChapter(UpdateView):
    model = Chapter
    fields = "__all__"


class AddChapter(CreateView):
    fields = "__all__"
    model = Chapter

class DeleteChapter(DeleteView):
    model = Chapter 
    success_url = reverse_lazy('english_grammar:chapter-list')

class PageDetail(DetailView):
    model = DetailView
