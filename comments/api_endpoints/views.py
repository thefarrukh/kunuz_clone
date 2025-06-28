from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  # Buni qo'shish juda muhim

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
