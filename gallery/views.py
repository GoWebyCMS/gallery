from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Gallery
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'gallery/list.html'
    context_object_name = 'latest_gallery_list'

    def get_queryset(self):
        return Gallery.objects.all()[:5]



class DetailView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/detail.html'

def gallery_detail(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)

    return render( request, 'gallery/detail.html', {'gallery': gallery})