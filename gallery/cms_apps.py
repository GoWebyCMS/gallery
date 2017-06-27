from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class GalleryApphook(CMSApp):
    app_name = "gallery"
    name = _("Gallery Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["gallery.urls"]

apphook_pool.register(GalleryApphook)  # register the applicationr the application