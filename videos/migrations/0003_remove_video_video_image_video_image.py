# Generated by Django 4.1 on 2023-11-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_remove_category_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_image',
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.FileField(null=True, upload_to='media/images/'),
        ),
    ]