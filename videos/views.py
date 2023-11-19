from django.shortcuts import render
from .models import (
    Category,
    Video,
    Like,
    Comment
)
from django.db.models import Count

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
    like = len(Like.objects.filter(type='like'))
    love = len(Like.objects.filter(type='love'))
    sad = len(Like.objects.filter(type='sad'))
    comments = Comment.objects.all()
    print(like)
    context['video'] = video
    context['videos'] = videos
    context['like'] = like
    context['love'] = love
    context['sad'] = sad
    context['user_icon'] = video.user.username[0]
    context['comments'] = comments

    return render(request, 'video.html', context)