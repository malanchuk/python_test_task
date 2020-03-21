from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from redirects_analyzer.views import (RedirectInfoView,
                                      RedirectView)


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # API urls
    path('api/', include(([
        path('analyzer/redirects/', RedirectView.as_view(), name="redirect"),
        path('analyzer/redirects/list/', 
            RedirectInfoView.as_view(), 
            name="redirect-list"),
        # path('analyzer/redirects/top_domains/', 
        #     RedirectInfoTopDomainsView.as_view(), 
        #     name="redirect-top-domains"),
    ], 'api'), namespace='api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Site Config
admin.sites.AdminSite.site_header = settings.ADMIN_SITE_HEADER
admin.sites.AdminSite.site_title = settings.ADMIN_SITE_TITLE
