from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'news', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
