from django.contrib import admin

from .models import Thread, Comment


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'post', 'author')
    list_filter = ('created_at', 'post', 'author')
    search_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'author', 'thread')
    list_filter = ('created_at', 'author', 'thread')
    search_fields = ('content',)


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
