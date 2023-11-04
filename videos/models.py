from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SharedFields(models.Model):
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        abstract = True


class Category(SharedFields):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=20)
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)


class Video(SharedFields):
    id = models.BigAutoField(primary_key=True)
    title_of_video = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    video_image = models.CharField(max_length=20)
    views = models.IntegerField()
    category = models.ForeignKey(Category,  models.SET_NULL, blank=True, null=True) 
    user = models.ForeignKey(User,  models.SET_NULL, blank=True, null=True)