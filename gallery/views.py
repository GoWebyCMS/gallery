from django.shortcuts import render
from django.views import generic
from .models import Gallery
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'gallery/list.html'
    context_object_name = 'latest_gallery_list'

    def get_queryset(self):
        return Gallery.objects.all()[:5]