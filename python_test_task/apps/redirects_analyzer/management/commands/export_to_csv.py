import csv

from django.core.management.base import BaseCommand

from redirects_analyzer.models import RedirectInfo
from redirects_analyzer.serializers import RedirectInfoSerializer


class Command(BaseCommand):
    """ 
    Generate CSV
    """
    def add_arguments(self, parser):
        parser.add_argument('--filename', dest='filename', default='redirects.csv') 

    def handle(self, *args, **options):
        with open(options['filename'], 'w') as output:
            redirects = RedirectInfo.objects.all()
            serializer = RedirectInfoSerializer(redirects, many=True)
            
            header = [f.name for f in RedirectInfo._meta.get_fields()]
            writer = csv.DictWriter(output, fieldnames=header)
            writer.writeheader()
            for row in serializer.data:
                writer.writerow(row)