from django.db import models

class Film(models.Model):
    swapi_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    film = models.ForeignKey(
        Film,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    author_name = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.author_name} on {self.film.title}"
