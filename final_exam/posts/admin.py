# Register your models here.
from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'author')
    list_filter = ('created_at', 'updated_at', 'author')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
