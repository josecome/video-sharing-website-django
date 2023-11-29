from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=20)    
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=20)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)    

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    title_of_video = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    link = models.SlugField(null=True) 
    image = models.FileField(upload_to="media/images/", null=True)
    views = models.IntegerField()
    tags = GenericRelation(Like)
    category = models.ForeignKey(Category,  models.SET_NULL, blank=True, null=True) 
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    tags = GenericRelation(Like)
    video = models.ForeignKey(Video, models.SET_NULL, related_name='comments', blank=True, null=True) 
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


class Share(models.Model):
    id = models.AutoField(primary_key=True)
    post_shared_link = models.CharField(max_length=80)
    post = models.ForeignKey(Video, related_name='shares', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField(null=True)

    class Meta:  
        db_table = "shares" 