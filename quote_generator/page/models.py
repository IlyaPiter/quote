from django.db import models

class Masterpiece(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return "'" + self.title + "' - " + self.author

class Quote(models.Model):
    content = models.TextField()
    source = models.ForeignKey(
        Masterpiece,
        on_delete=models.CASCADE,
        related_name='masterpieces',
    )
    value = models.IntegerField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('content', 'source'),
                name='Unique quote constraint',
            ),
        )


    def __str__(self):
        return self.content