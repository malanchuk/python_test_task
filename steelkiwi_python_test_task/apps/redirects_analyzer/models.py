from django.db import models

from django_extensions.db.models import TimeStampedModel


class RedirectInfo(TimeStampedModel):
    """ 
    Model to store info of all redirects.
    """
    redirect_full_url = models.URLField(max_length=500)
    redirect_domain_name = models.CharField(max_length=100)
    redirect_get_paramenters = models.CharField(max_length=500)
    
    referrer_full_url = models.URLField(max_length=500)
    referrer_domain_name = models.CharField(max_length=100)
    
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.redirect_full_url
