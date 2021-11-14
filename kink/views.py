from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Storage, Video, Bookmark
from django.contrib import messages
from django.urls import reverse
from django.core import serializers

# Create your views here.
def home(request):
    videos = Video.objects.all()
    last_seen_video = videos.order_by('-last_seen_at').first()
    context = {
        'videos': videos.order_by('title'),
        'last_seen_video': last_seen_video
    }
    return render(request, 'kink/home.html', context=context)

def video(request, id):
    video = Video.objects.filter(id=id).first()
    if video:
        next_v = Video.objects.filter(title__gt=video.title).order_by('title').first()
        pre_v = Video.objects.filter(title__lt=video.title).order_by('-title').first()
        context = {
            'video': video,
            'next': next_v,
            'prev': pre_v
        } 
        return render(request, 'kink/video.html', context=context)
    else:
        messages.warning(request, 'Video not found')
        redirect_path = reverse('home-page')
        return redirect(redirect_path)


def bookmark(request):
    try:
        if request.method=='POST':
            video_id = request.POST.get('vid')
            bookmark_text = request.POST.get('btext')
            bookmark_time = request.POST.get('btime')
            video = Video.objects.filter(id=video_id).first()
            if video:
                bookmark = Bookmark.objects.create(video=video, text=bookmark_text, time=bookmark_time)
                return JsonResponse({"status": "success", "text": f'Bookmark added at {bookmark_time}'})
    except:
        pass 

def bookmarks(request, id):
    video = Video.objects.filter(id=id).first()
    bookmarks = Bookmark.objects.filter(video=video).order_by('-time')
    data = serializers.serialize('json', bookmarks)
    return HttpResponse(data, content_type="application/json")


def last_seen(request):
    try:
        if request.method=='POST':
            video_id = request.POST.get('vid')
            last_seen = request.POST.get('last_seen')
            video = Video.objects.filter(id=video_id).first()
            if video:
                video.upate_last_seen_at(last_seen)
                return JsonResponse({"status": "success"})
    except:
        pass  


def remove_bookmark(request):
    try:
        if request.method=='POST':
            video_id = request.POST.get('vid')
            bookmark_id = request.POST.get('bid')
            video = Video.objects.filter(id=video_id).first()
            if video:
                bookmark = Bookmark.objects.filter(id=bookmark_id).first()
                if bookmark:
                    bookmark.delete()
                    bookmarks = Bookmark.objects.filter(video=video).order_by('-time')
                    return JsonResponse({"status": "success", "bookmarks": bookmarks})
    except:
        pass  


def update_bookmark(request):
    try:
        if request.method=='POST':
            video_id = request.POST.get('vid')
            bookmark_id = request.POST.get('bid')
            bookmark_text = request.POST.get('btext')
            video = Video.objects.filter(id=video_id).first()
            if video:
                bookmark = Bookmark.objects.filter(id=bookmark_id).first()
                if bookmark:
                    bookmark.text = bookmark_text
                    bookmark.save() 
                    bookmarks = Bookmark.objects.filter(video=video).order_by('-time')
                    return JsonResponse({"status": "success", "bookmarks": bookmarks})
    except:
        pass  


def update_raw_link(request):
    try:
        if request.method=='POST':
            video_id = request.POST.get('vid')
            raw_link = request.POST.get('raw_link')
            video = Video.objects.filter(id=video_id).first()
            if video:
                video.update_raw_link(raw_link)
                return JsonResponse({"status":"success"})
    except:
        pass  


def update_mf_link(request):
    try:
        if request.method=='POST':
            video_id = request.POST.get('vid')
            mf_link = request.POST.get('mf_link')
            video = Video.objects.filter(id=video_id).first()
            if video:
                video.update_mf_link(mf_link)
                return JsonResponse({"status":"success"})
    except:
        pass  



from kink.models import Video
a_vs= Video.objects.all()
my_list = []
for v in a_vs:
    my_dict = {'title': v.title, 'last_seen_at': v.last_seen_at, 'storage_email': v.storage.email, 'storage_pass': v.storage.password, 'mf_link': v.mf_link, 'video_link': v.raw_link, 'desc': v.description }
    my_list.append(my_dict)
print(my_list)