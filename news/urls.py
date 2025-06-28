from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.api_endpoints.views import NewsViewSet


router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]
