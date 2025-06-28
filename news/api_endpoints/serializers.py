from rest_framework import serializers
from news.models import Category, Tag, MediaFile, News
from accounts.models import User  # agar kerak bo'lsa

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # faqat o'qish uchun
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = MediaFileSerializer(many=True, read_only=True)
    liked_by = serializers.StringRelatedField(many=True, read_only=True)  # o'qish uchun

    class Meta:
        model = News
        fields = '__all__'
