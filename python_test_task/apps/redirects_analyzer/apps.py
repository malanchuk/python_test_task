from contextlib import suppress

from django.apps import AppConfig


class RedirectsAnalyzerAppConfig(AppConfig):
    name = 'redirects_analyzer'
    verbose_name = 'Redirects Analyzer'
