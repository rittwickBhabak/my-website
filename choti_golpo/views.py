from django.http.response import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView 
from .models import Story, DirtyTalk
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class StoryList(ListView):
    model = Story
    queryset = Story.objects.all().order_by('is_read')


class StoryDetail(DetailView):
    model = Story 

class DeleteStory(DeleteView):
    model = Story 
    success_url = reverse_lazy('index')

class UpdateStory(UpdateView):
    fields = ('title', 'text')
    model = Story 

class CreateStory(CreateView):
    fields = ('title', 'text')
    model = Story 

class DirtyTalkList(ListView):
    paginate_by = 10
    model = DirtyTalk 

class DeleteTalkView(DeleteView):
    model = DirtyTalk
    success_url = reverse_lazy('talk-list')

def add_dirty_talk(request):
    if request.method == 'POST':
        talk = request.POST.get('talk')
        height = request.POST.get('last_height')
        s_id = request.POST.get('s_id')
        story = get_object_or_404(Story, pk=s_id)
        story.last_height = height
        story.save()

        if len(talk)>0:
            DirtyTalk.objects.create(text = talk)

            return JsonResponse({"status": "success"})


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            messages.error(request, 'User does not exist')
            return redirect(reverse('login'))
    else:
        return render(request, 'myapp/login.html')


def upload_online(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('story')

        Story.objects.create(title=title, text=text)

        return JsonResponse({"status": "success"})

def story_completed(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        story = get_object_or_404(Story, pk=int(s_id))
        story.is_read = True 
        story.save()
        success_message = f"Congratulations! {story.title} Completed."
        messages.success(request, success_message)
        return redirect(reverse('index'))
        

def edit_talk(request):
    if request.method == 'POST':
        talk_id = request.POST.get('talk_id')
        text = request.POST.get('text')

        talk = get_object_or_404(DirtyTalk, pk=talk_id)

        talk.text = text 
        talk.save()
        new_text = talk.text
        return JsonResponse({"status": "success", "text": new_text})