from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, Category, Tag, MediaFile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_type', 'file', 'uploaded_at')
    list_filter = ('media_type',)
    search_fields = ('file',)

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'is_active', 'views_count')
    list_filter = ('author', 'is_active', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories', 'tags', 'images', 'liked_by')
