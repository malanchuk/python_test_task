from django.contrib import admin

from .models import RedirectInfo


@admin.register(RedirectInfo)
class RedirectInfoAdmin(admin.ModelAdmin):
    search_fields = ('redirect_domain_name', 'referrer_domain_name',)
    list_filter = ('browser', 'os', 'created', 'modified', )
    list_display = ('redirect_full_url', 'referrer_domain_name',
                    'browser', 'os', 'created')
