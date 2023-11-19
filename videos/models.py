from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=20)    
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    title_of_video = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.FileField(upload_to="media/images/", null=True)
    views = models.IntegerField()
    category = models.ForeignKey(Category,  models.SET_NULL, blank=True, null=True) 
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    video = models.ForeignKey(Video,  models.SET_NULL, blank=True, null=True) 
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    video = models.ForeignKey(Video,  models.SET_NULL, blank=True, null=True)
    comment = models.ForeignKey(Comment,  models.SET_NULL, blank=True, null=True) 
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)