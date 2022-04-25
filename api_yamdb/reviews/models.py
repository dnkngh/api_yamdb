from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Введите текст отзыва.'
    )
    text = models.TextField(blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва.'
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(10)
        ),
        verbose_name='Оценка произведения.'
    )
    pub_date = models.DateTimeField('Дата отзыва', auto_now_add=True)

    class Meta:
        unique_together = ['title_id', 'author']

    def __str__(self):
        return f'Title: {self.title_id} | Author: {self.author}'


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(
        help_text='Введите текст комментария.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария.'
    )
    pub_date = models.DateTimeField('Дата комментария', auto_now_add=True)

    def __str__(self):
        return f'Review: {self.review_id} | {self.text[:10]}'
