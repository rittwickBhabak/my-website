from django.views.generic import TemplateView 
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class HomeView(TemplateView):
    template_name= 'home.html'

def logout_view(request):
    logout(request)
    return redirect(reverse('home-page'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home-page'))
        else:
            messages.error(request, 'User does not exist')
            return redirect(reverse('home-page'))
    else:
        return render(request, 'login.html')