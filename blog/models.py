from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


class Post(models.Model):

    """
        Blog Post model
    """

    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name="posts")
    content = models.TextField()

    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(
        'Category', related_name='posts', null=True, blank=True
        )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return "%s" %(self.title)


    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])


class Category(models.Model):

    """
        Category Model
    """

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name',]

    def __unicode__(self):
        return self.name
