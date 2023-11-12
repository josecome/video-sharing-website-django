from django.shortcuts import render
from .models import (
    Category,
    Video
)

# Create your views here.

def home(request):
    context = {}
    videos = Video.objects.all()[:6].select_related('user')
    context['videos'] = videos
    return render(request, 'home.html', context)


def video_detail(request, id):
    context = {}
    video = Video.objects.get(id=id)
    # videos = Video.objects.filter(id=id).select_related('user')
    videos = Video.objects.all()[:6].select_related('user')
    context['video'] = video
    context['videos'] = videos
    return render(request, 'video.html', context)