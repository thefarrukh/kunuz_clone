from rest_framework import viewsets
from news.models import Category, Tag, MediaFile, News
from .serializers import (
    CategorySerializer, TagSerializer,
    MediaFileSerializer, NewsSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
