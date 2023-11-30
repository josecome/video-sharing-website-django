from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse as Response
from rest_framework import status
from django.db.models import Q, Count
from datetime import date, datetime
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


class CommentModelViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        server_data = {'user': request.user.id, 'date_created': date.today(), 'date_updated': date.today()}
        comment_data = request.data

        serializer = self.serializer_class(data = { **server_data, **comment_data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
