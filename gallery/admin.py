from django.contrib import admin

from .models import Gallery, Image

# Register your models here.


class ImageInline(admin.StackedInline):
    model = Image


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Gallery, GalleryAdmin)