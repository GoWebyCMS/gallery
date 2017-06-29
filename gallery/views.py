from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Gallery, GalleryImage
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'gallery/list.html'
    context_object_name = 'latest_gallery_list'

    def get_queryset(self):
        return Gallery.objects.all()


class DetailView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/detail.html'

def gallery_detail(request, gallery_slug):
    gallery = None
    galleries = Gallery.objects.all()
    gallery_images = GalleryImage.objects.all()

    ''' Filter images - get images per gallery'''
    if gallery_slug:
        gallery = get_object_or_404(Gallery, slug=gallery_slug)
        gallery_images = gallery_images.filter(gallery=gallery)

    return render( request, 'gallery/detail.html', {
        'gallery': gallery,
        'galleries': galleries,
        'gallery_images': gallery_images
    })
