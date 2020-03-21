from django.db import models

from django_extensions.db.models import TimeStampedModel


class RedirectInfo(TimeStampedModel):
    """ 
    Model to store info of all redirects.
    """
    redirect_full_url = models.URLField(max_length=500)
    redirect_domain_name = models.CharField(max_length=100)
    redirect_query = models.CharField(max_length=500, blank=True)
    referrer_full_url = models.URLField(max_length=500, blank=True)
    referrer_domain_name = models.CharField(max_length=100, blank=True)
    
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=50, blank=True)
    os = models.CharField(max_length=50, blank=True)
    platform = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.redirect_full_url
