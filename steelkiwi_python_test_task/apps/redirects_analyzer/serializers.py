from rest_framework import serializers

from .models import RedirectInfo


class RedirectInfoSerializer(serializers.ModelSerializer):
    """ 
    Model serializer for the listing of redirects.
    """
    class Meta:
        model = RedirectInfo
        fields = '__all__'


class RedirectInfoStatsSerializer(serializers.ModelSerializer):
    """ 
    Model serializer for the grouped redirects stats.
    """
    redirect_url = serializers.URLField()
    redirects = serializers.IntegerField()
    referrers = serializers.ListField()
    last_redirected = serializers.DateTimeField()

    class Meta:
        model = RedirectInfo
        fields = ('redirect_url', 'redirects', 'referrers', 'last_redirected')


class RedirectInfoTopSerializer(serializers.ModelSerializer):
    """ 
    Simple serializer for the list of top domains.
    """
    redirect_domain_name = serializers.CharField()
    redirects = serializers.IntegerField()

    class Meta:
        model = RedirectInfo
        fields = ('redirect_domain_name', 'redirects')
