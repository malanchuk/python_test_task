import httpagentparser
from urllib.parse import urlparse

from celery import shared_task

from .models import RedirectInfo

@shared_task
def save_redirect_info_task(redirect_to, referrer='', ip='', user_agent=''):
    """ 
    Parse redirect request data and save it to db
    """
    parsed_redirect_to = urlparse(redirect_to)
    if referrer:
        parsed_referrer = urlparse(referrer)
        referrer_domain_name = parsed_referrer.netloc
    else:
        referrer_domain_name = ''
    
    ua = httpagentparser.detect(user_agent)
    browser = ''
    if ua.get('browser'):
        browser = " ".join([ua['browser'].get('name',''),
                           ua['browser'].get('version','')]).strip()
    platform = ''
    if ua.get('browser'):
        platform = " ".join([ua['platform'].get('name',''),
                        ua['platform'].get('version','')]).strip()
    os = ''
    if ua.get('os'):
        os = " ".join([ua['os'].get('name',''),
                    ua['os'].get('version','')]).strip()

    redirect_obj = RedirectInfo(
        redirect_full_url=redirect_to,
        redirect_domain_name=parsed_redirect_to.netloc,
        redirect_query=parsed_redirect_to.query,
        referrer_full_url=referrer,
        referrer_domain_name=referrer_domain_name,
        ip_address=ip,
        browser=browser,
        platform=platform,
        os=os,
    )
    redirect_obj.save()