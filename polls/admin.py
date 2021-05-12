from django.contrib import admin

from .models import Post, Comment, User_Table

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User_Table)
