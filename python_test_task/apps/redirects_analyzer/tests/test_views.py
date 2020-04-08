import pytest
from mixer.backend.django import mixer

from django.conf import settings
from django.urls import reverse

from redirects_analyzer.models import RedirectInfo

settings.CELERY_TASK_ALWAYS_EAGER = True
pytestmark = pytest.mark.django_db


class TestRedirectView:
    def test_redirect(self, api_client):
        response = api_client.post(reverse('api:redirect'), {
            'to': 'http://test.com',
        })
        assert response.status_code == 302, \
            "Should redirect to the given page"
        assert RedirectInfo.objects.count() == 1, \
            "Should save redirect info into database"
    
    def test_redirect_empty_arg(self, api_client):
        response = api_client.post(reverse('api:redirect'),)
        assert response.status_code == 404, \
            "Post parameters should be required"


class TestRedirectInfoListView:
    def test_list(self, api_client):
        mixer.cycle(5).blend('redirects_analyzer.RedirectInfo',)
        response = api_client.get(reverse('api:redirect-list'))
        
        assert response.status_code == 200
        assert response.data.get('count') == 5, \
            "Should return list of all objects"


class TestRedirectInfoStatsView:
    def test_list(self, api_client):
        mixer.cycle(5).blend('redirects_analyzer.RedirectInfo', 
            redirect_full_url='http://test.com')
        mixer.cycle(5).blend('redirects_analyzer.RedirectInfo', )
        response = api_client.get(reverse('api:redirect-stats'))
        assert response.status_code == 200
        assert response.data.get('count') == 6, \
            "Should return aggregated data"


class TestRedirectInfoTopView:
    def test_list(self, api_client):
        mixer.cycle(25).blend('redirects_analyzer.RedirectInfo', )
        response = api_client.get(reverse('api:redirect-top'))
        assert response.status_code == 200
        assert response.data.get('count') == 10, \
            "Should return only top 10 rows"