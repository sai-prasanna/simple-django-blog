from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Post(models.Model):

    """
        Blog Post model
    """

    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name="posts")
    content = models.TextField()

    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.slug


class Category(models.Model):

    """
        Category Model
    """

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
