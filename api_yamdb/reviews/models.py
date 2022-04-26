from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение.',
        help_text='Введите текст отзыва.'
    )
    text = models.TextField(max_length=300)
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
        error_messages={
            'validator': 'Оценка должна быть в диапазоне от 0 до 10.'
        },
        verbose_name='Оценка произведения.'
    )
    pub_date = models.DateTimeField('Дата отзыва', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('pub_date',)
        unique_together = ['title', 'author']

    def __str__(self):
        return f'Title: {self.title} | Author: {self.author}'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        verbose_name='Отзыв.'
    )
    text = models.TextField(
        max_length=300,
        null=False,
        help_text='Введите текст комментария.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        verbose_name='Автор комментария.'
    )
    pub_date = models.DateTimeField('Дата комментария', auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (
            f'Review: {self.review} | Comment Author:'
            f' {self.author.username} | {self.text[:10]}'
        )
