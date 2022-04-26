from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from reviews.models import Category, Comment, Genre, Review, Title


class CommentSerialier(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault
    )

    class Meta:
        model = Comment
        exclude = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    title_id = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Title.objects.all()
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault,
        read_only=True
    )

    def validate(self, data):
        if self.context['request'].method == 'POST':
            user = self.context['request'].user
            title_id = self.context['view'].kwargs.get('title_id')
            if Review.objects.filter(author=user, title_id=title_id).exists():
                raise ValidationError(
                    'Вы уже написали отзыв на это произведение'
                )

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('author', 'title_id')
