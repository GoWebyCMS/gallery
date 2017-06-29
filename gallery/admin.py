from django.contrib import admin

from .models import Gallery, GalleryImage

# Register your models here.


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline, ]
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Gallery, GalleryAdmin)