# Generated by Django 4.1 on 2023-11-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_comment_video_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.SlugField(null=True),
        ),
    ]
