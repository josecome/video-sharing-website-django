from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from videos.models import (
    Video,
    Comment,
)

from .serializer import (
    VideoSerializer,
    CommentSerializer,
    )

class HomeViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class VideoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = VideoSerializer
    queryset = Video.objects.all()