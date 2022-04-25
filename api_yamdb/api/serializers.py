from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title


class CommentSerialier(serializers.ModelSerializer):
    pass

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author',)


class ReviewSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('author',)

    def validate(self, data):
        # валидация уникальности "произведение-автор отзыва"
