from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post

class PostList(ListView):
    model = Post 

class PostDetail(DetailView):
    model = Post 

class PostEdit(UpdateView):
    model = Post 
    fields = "__all__"

class PostDelete(DeleteView):
    model = Post 

class PostAdd(CreateView):
    model = Post 
    fields = "__all__"