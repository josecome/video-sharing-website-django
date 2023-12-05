from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from videos.models import Video, Comment


def is_admin(user):
    return User.objects.filter(is_superuser=1).exists()


admin_required = user_passes_test(is_admin)


def user_is_video_author(function):
    def wrap(request, *args, **kwargs):
        entry = Video.objects.get(pk=kwargs['user_id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_comment_author(function):
    def wrap(request, *args, **kwargs):
        entry = Comment.objects.get(pk=kwargs['user_id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap