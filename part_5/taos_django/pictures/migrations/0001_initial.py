# Generated by Django 2.2.3 on 2019-07-20 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PicturePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to=pictures.models.user_directory_path)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('num_likes', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=144)),
                ('picture_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pictures.PicturePost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
