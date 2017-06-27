from django.db import models
from filer.fields.image import FilerImageField


# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    featured_image = FilerImageField(related_name="featured")

    def __str__(self):
        return self.title

class Image(models.Model):
    image_file = FilerImageField()
    obj = models.ForeignKey(Gallery)
