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
        on_delete=models.CASCADE
    )
    value = models.IntegerField()

    def __str__(self):
        return self.content