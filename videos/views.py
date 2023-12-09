from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from .models import (
    Category,
    Video,
    Like,
    Comment
)
from django.db.models import Count
from django.db.models import Q

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
    like = len(Like.objects.filter(tag='like'))
    love = len(Like.objects.filter(tag='love'))
    sad = len(Like.objects.filter(tag='sad'))
    comments = Comment.objects.filter(video_id=id).annotate(
        count_likes=Count("tags", filter=Q(tags__tag='like')),
        count_loves=Count("tags", filter=Q(tags__tag='love')),
        count_sads=Count("tags", filter=Q(tags__tag='sad')),
        )
    
    context['video'] = video
    context['videos'] = videos
    context['like'] = like
    context['love'] = love
    context['sad'] = sad
    context['user_icon'] = video.user.username[0]
    context['comments'] = comments

    return render(request, 'video.html', context)


def studio(request):
    return render(request, 'studio.html')


def loginPage(request):
    if request.user.is_authenticated:
        messages.success(request, _('AAAA'))
        return redirect('/')
    else:    
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            # admin, password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                messages.success(request, _('Successfull logged in'))
                return redirect('/')           
            else:
                # Return an 'invalid login' error message.
                messages.info(request, _('Please, Invalid Username and Password!'))
            
    return render(request, 'login.html')


def registrationPage(request):
    form = CreateUserForm()
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.sucess(request, 'Account was sucessfully created for ' + user)      
            send_email(request)
            
            return redirect('login.html')
                                
    context = {'form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
        
    return render(request,'logout.html')    
