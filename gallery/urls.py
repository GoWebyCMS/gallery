from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^gallery/(?P<slug>[-\w\d]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.gallery_detail, name='gallery_detail'),

]
