from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.documentation import include_docs_urls

from redirects_analyzer.views import (RedirectView,
                                      RedirectInfoListView,
                                      RedirectInfoStatsView,
                                      RedirectInfoTopView)


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path('docs/', include_docs_urls(title='Redirects analyzer API', public=False)),
    # API urls
    path('api/', include(([
        path('analyzer/redirects/', RedirectView.as_view(), name="redirect"),
        path('analyzer/redirects/list/', 
            RedirectInfoListView.as_view(), 
            name="redirect-list"),
        path('analyzer/redirects/stats/', 
            RedirectInfoStatsView.as_view(), 
            name="redirect-stats"),
        path('analyzer/redirects/top/', 
            RedirectInfoTopView.as_view(), 
            name="redirect-top"),
    ], 'api'), namespace='api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Site Config
admin.sites.AdminSite.site_header = settings.ADMIN_SITE_HEADER
admin.sites.AdminSite.site_title = settings.ADMIN_SITE_TITLE
