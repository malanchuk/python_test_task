from datetime import timedelta
from django.http import Http404, HttpResponseRedirect
from django.db.models import Count, Max, F, Q, Value, URLField
from django.db.models.functions import Replace, Concat
from django.contrib.postgres.aggregates import ArrayAgg
from django.utils import timezone

from rest_framework import mixins
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .models import RedirectInfo
from .serializers import (RedirectInfoSerializer, 
                          RedirectInfoStatsSerializer,
                          RedirectInfoTopSerializer)
from .tasks import save_redirect_info_task


class RedirectView(APIView):
    """
    View to save redirect info and make a redirect itself.
    """
    def post(self, request):
        """
        Save redirect info async with the celery task and make redirect
        """
        redirect_to = request.data.get('to')
        if not redirect_to:
            raise Http404
        referrer = request.META.get('HTTP_REFERER', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        ip = request.META.get('REMOTE_ADDR', '')
        save_redirect_info_task.apply_async(
            args=(redirect_to, referrer, ip, user_agent)
        )
        return HttpResponseRedirect(redirect_to)


class RedirectInfoListView(ListAPIView):
    """ 
    View to get the list of all registered redirects 
    with search, filters and ordering options.
    """
    queryset = RedirectInfo.objects.all()
    serializer_class = RedirectInfoSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter, 
    ]
    search_fields = ['redirect_domain_name', 'referrer_domain_name']
    filterset_fields = ['redirect_domain_name', 'referrer_domain_name']


class RedirectInfoStatsView(ListAPIView):
    """
    View to get aggregated statistics about redirects.
    Endpoint returns the list of performed redirects grouped by 
    full urls without get parameters. 
    Annotated by the number of unique records 
    of redirects with full url and contains
    a list of referrers of the redirect, 
    and the date and time of the latest redirect.
    """
    queryset = RedirectInfo.objects.all()
    serializer_class = RedirectInfoStatsSerializer

    def get_queryset(self):
        """
        Custom aggregation queryset
        """
        return RedirectInfo.objects.annotate(
                    redirect_url=Replace(
                        F('redirect_full_url'), 
                        Concat(Value('?'), F('redirect_query')), 
                        output_field=URLField()
                    )
                ).values('redirect_url').order_by('redirect_url').annotate(
                    redirects=Count('redirect_url'), 
                    last_redirected=Max('created'),
                    referrers=ArrayAgg(
                        F('referrer_domain_name'), 
                        filter=Q(referrer_domain_name__gt='')
                    ),
                )


class RedirectInfoTopView(ListAPIView):
    """
    View to get the list of top domains
    for which redirects were made this month.
    """
    serializer_class = RedirectInfoTopSerializer
    max_domains = 10

    def get_queryset(self):
        last_month = timezone.now()-timedelta(days=30)
        top_domains = RedirectInfo.objects.filter(
                created__gte=last_month,
            ).values('redirect_domain_name')\
             .order_by('redirect_domain_name').annotate(
                redirects=Count('redirect_domain_name'),
            ).order_by('-redirects')
        return top_domains[:self.max_domains]