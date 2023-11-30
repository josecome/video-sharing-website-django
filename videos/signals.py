from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from videos.models import (
    Category,
    Video,
    Comment,
    Like,
    Share,
)


@receiver(post_save, sender=Category)
def user_created(sender, instance, created, **kwargs):
   if created:
      print('New Category created:', instance.category)


@receiver(post_save, sender=Video)
def user_created(sender, instance, created, **kwargs):
   if created:
      print('New Video created:', instance.title_of_video)


@receiver(post_save, sender=Comment)
def user_created(sender, instance, created, **kwargs):
   if created:
      print('New Comment created:', instance.comment)


@receiver(post_save, sender=Like)
def user_created(sender, instance, created, **kwargs):
   if created:
      print('New Like added:', instance.tag)


@receiver(post_save, sender=Share)
def user_created(sender, instance, created, **kwargs):
   if created:
      print('New Share created:', instance.date_created)