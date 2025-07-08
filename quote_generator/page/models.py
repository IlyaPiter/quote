from django.db import models


class Masterpiece(models.Model):
    title = models.CharField('Название произведения', max_length=255)
    author = models.CharField('Автор произведения', max_length=255)

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return "'" + self.title + "' - " + self.author


class Quote(models.Model):
    content = models.TextField(
        'Цитата', help_text='Цитата из фильма или книги')
    source = models.ForeignKey(
        Masterpiece,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
        related_name='masterpieces',
        help_text='Источник цитаты',
    )
    value = models.IntegerField(
        'Вес цитаты',
        help_text="""Чем выше вес, тем больше шанс выдачи этой
         цитаты на заглавной странице""",
        )
    views = models.IntegerField('Количество просмотров', default=0)
    likes = models.IntegerField('Количество лайков', default=0)
    dislikes = models.IntegerField('Количество дизлайков', default=0)

    class Meta:
        verbose_name = 'цитата'
        verbose_name_plural = 'Цитаты'
        constraints = (
            models.UniqueConstraint(
                fields=('content', 'source'),
                name='Unique quote constraint',
            ),
        )
        ordering = ('-likes',)

    def __str__(self):
        return str(self.content)
