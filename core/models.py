from django.db import models
from django.contrib.auth.models import User


# MODEL 1
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# MODEL 2
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# MODEL 3
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # MANY-TO-ONE RELATIONSHIP
    # Many posts → One category
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    # MANY-TO-MANY RELATIONSHIP
    # Many posts ↔ Many tags
    tags = models.ManyToManyField(Tag, blank=True)

    # AUTHOR RELATIONSHIP
    # Many posts → One user
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
