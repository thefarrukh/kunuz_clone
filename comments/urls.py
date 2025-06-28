from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comments.api_endpoints.views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
