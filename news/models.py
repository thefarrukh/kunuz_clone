from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class MediaFile(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    )

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='uploads/media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type}: {self.file.name}"

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news')
    categories = models.ManyToManyField('Category', related_name='news')
    tags = models.ManyToManyField('Tag', related_name='news')
    images = models.ManyToManyField('MediaFile', related_name='news', blank=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_news', blank=True)

    is_active = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
