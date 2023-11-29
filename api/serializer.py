from rest_framework import serializers
from videos.models import (
    Video,
    Comment,
)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["comment"]


class VideoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    comments = CommentSerializer(read_only=True, many=True)
    count_likes = serializers.IntegerField()
    count_loves = serializers.IntegerField()
    count_sads = serializers.IntegerField()
    count_comments = serializers.IntegerField()
    count_shares = serializers.IntegerField()
    
    class Meta:        
        model = Video
        fields = ["id", "title_of_video", "description", "link","image", "views", "username", "category", "first_name", "last_name", "created_date", "comments", "count_likes", "count_loves", "count_sads", "count_shares", "count_comments"]
