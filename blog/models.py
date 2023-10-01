from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title
