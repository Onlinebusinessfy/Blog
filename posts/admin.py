from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "subtitle", "author"
    ]

admin.site.register(Post, PostAdmin)