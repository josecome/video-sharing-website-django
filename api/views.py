from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count
from videos.models import (
    Video,
    Comment,
)

from .serializer import (
    VideoSerializer,
    CommentSerializer,
    )

class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all().annotate(
        count_likes=Count("tags", filter=Q(tags__tag='like')),
        count_loves=Count("tags", filter=Q(tags__tag='love')),
        count_sads=Count("tags", filter=Q(tags__tag='sad')),
        count_comments=Count("comments"),
        count_shares=Count("shares"),
        )[:12]


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all().annotate(
        count_likes=Count("tags", filter=Q(tags__tag='like')),
        count_loves=Count("tags", filter=Q(tags__tag='love')),
        count_sads=Count("tags", filter=Q(tags__tag='sad')),
        count_comments=Count("comments"),
        count_shares=Count("shares"),
        )[:1]
    
    def get_queryset(self):
        link = self.kwargs['link']
        if link:
            self.queryset = Video.objects.filter(link=link).annotate(
                count_likes=Count("tags", filter=Q(tags__tag='like')),
                count_loves=Count("tags", filter=Q(tags__tag='love')),
                count_sads=Count("tags", filter=Q(tags__tag='sad')),
                count_comments=Count("comments"),
                count_shares=Count("shares"),
            )
            return self.queryset
        else:
            return self.queryset

