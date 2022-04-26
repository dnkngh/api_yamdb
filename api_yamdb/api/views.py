from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Comment, Review, Title
from .serializer import CommentSerializer, ReviewSerializer


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = int(self.kwargs.get('review_id'))
        review = get_object_or_404(Review, pk=review_id)
        return review.comments

    def get_permissions(self):
        # предусмотреть пермишены для модератора, если self.action == retrieve

    def preform_create(self, serializer):
        review_id = int(self.kwargs.get('review_id'))
        review = get_object_or_404(Review, pk=review_id)
        user = self.request.user
        serializer.save(author=user, review=review)

class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title_id = int(self.kwargs.get('title_id'))
        title = get_object_or_404(Title, pk=title_id)
        return title.reviews

    def get_permissions(self):
        # предусмотреть пермишены для модератора, если self.action == retrieve

    def perform_create(self, serializer):
        title_id = int(self.kwargs.get('title_id'))
        title = get_object_or_404(Title, pk=title_id)
        user = self.request.user
        serializer.save(author=user, title=title)
