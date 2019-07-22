from django.contrib import admin

from pictures.models import Comment, PicturePost

admin.site.register(PicturePost)
admin.site.register(Comment)
