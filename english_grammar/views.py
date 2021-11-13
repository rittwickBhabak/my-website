from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
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

def page_detail(request, chapter_id, page_no):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    if 1 <= page_no and page_no <= chapter.total_pages:
        if page_no==chapter.total_pages:
            next_page_no = 1
        else:
            next_page_no = page_no + 1
        if page_no == 1:
            prev_page_no = chapter.total_pages
        else:
            prev_page_no = page_no - 1
        return render(request, 'english_grammar/page_detail.html', {'chapter': chapter, 'page_no': page_no, 'next_page_no': next_page_no, 'prev_page_no': prev_page_no})
    else:
        return redirect('english_grammar:chapter-list')
