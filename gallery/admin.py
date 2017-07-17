from django.contrib import admin

from .models import Gallery, GalleryImage, Category

# Register your models here.


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline, ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)