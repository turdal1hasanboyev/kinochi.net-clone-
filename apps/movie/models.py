from django.db import models

from django.utils.text import slugify

from django.urls import reverse

import uuid

from ckeditor.fields import RichTextField

from ..common.models import BaseModel
from apps.category.models import Category, Tag
from apps.user.models import User


class Movie(BaseModel):
    """
    Movie model
    """

    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True,
                            blank=True, null=True, db_index=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_movie')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag_movie')
    views = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to='movies', blank=True, null=True)
    premiere_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_movie')
    from_the_movie = models.CharField(max_length=300)
    description = RichTextField(null=True, blank=True)
    trailer = models.FileField(upload_to='trailers', blank=True, null=True)

    class Meta:
        """
        Meta class for Movie model
        """

        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def get_absolute_url(self, *args, **kwargs):
        """"
        Get absolute url for movie."
        """

        return reverse('movie-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """"
        Save movie instance.
        """

        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of Movie model.
        """

        return f"{self.name}"
