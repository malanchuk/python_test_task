from rest_framework import serializers

from .models import RedirectInfo


class RedirectInfoSerializer(serializers.ModelSerializer):
    """ 
    Model serializer for the listing of RedirectInfo model.
    """
    class Meta:
        model = RedirectInfo
        fields = '__all__'