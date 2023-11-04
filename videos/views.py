from django.shortcuts import render
from models import (
    Category,
    Video
)

# Create your views here.

def home(request):
    context = {}
    videos = Video.objects.all()[:8]
    context['videos'] = videos
    return render(request, 'home.html', context)