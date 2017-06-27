from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^gallery$', views.IndexView.as_view(), name='index'),
    #url(r'^work/(?P<category_slug>[-\w]+)/$', views.portfolio_list, name='portfolio_list'),
    # url(r'^project/(?P<slug>[\w-]+)/$', views.portfolio_detail, name='portfolio_detail'),
    #url(r'^about/$', views.about, name='about'),
    #url(r'^contact/', include('contact_form.urls')),
]
