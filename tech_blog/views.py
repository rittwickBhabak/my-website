from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post
from django.urls import reverse_lazy 

class PostList(ListView):
    model = Post 

class PostDetail(DetailView):
    model = Post 

class PostEdit(UpdateView):
    model = Post 
    fields = "__all__"

class PostDelete(DeleteView):
    model = Post 
    success_url = reverse_lazy('tech_blog:post-list')

class PostAdd(CreateView):
    model = Post 
    fields = "__all__"