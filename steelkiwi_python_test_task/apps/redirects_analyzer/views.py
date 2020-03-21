from django.http import Http404, HttpResponseRedirect

from rest_framework import mixins
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import RedirectInfo
from .serializers import RedirectInfoSerializer
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


class RedirectInfoView(ListAPIView):
    """ 
    ViewSet to get statistic information about redirects.
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

