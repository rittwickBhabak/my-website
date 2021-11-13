from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Restaurant


class AddRestaurant(CreateView):
    fields = ('title', 'description', 'location')
    model = Restaurant

class RestaurantList(ListView):
    model = Restaurant

class RestaurantDetail(DetailView):
    model = Restaurant

class EditRestaurant(UpdateView):
    model = Restaurant
    fields = "__all__"

class DeleteRestaurant(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurants:restaurant-list')

