# Generated by Django 4.1 on 2023-11-28 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_rename_type_like_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='videos.video'),
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_shared_link', models.CharField(max_length=80)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to='videos.video')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shares',
            },
        ),
    ]
