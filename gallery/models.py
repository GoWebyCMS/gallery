from django.db import models

from filer.fields.image import FilerImageField
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse('category_list',args=[self.slug])

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='works', default=1)
    slug = models.SlugField(unique=True)
    featured_image = FilerImageField(related_name="featured")

    class Meta:
        ordering = ('title',)
        verbose_name = "gallery"
        verbose_name_plural = "Galleries"

    @models.permalink
    def get_absolute_url(self):
        return ('details', (), {'slug': self.slug})

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image_file = FilerImageField(related_name='gallery_images')
    gallery = models.ForeignKey(Gallery)