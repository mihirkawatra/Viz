from django.core.management.base import BaseCommand, CommandError
from api_request.models import Entry

class Command(BaseCommand):
    help="Shows all codes"

    def handle(self, *args, **options):
        qs = Entry.objects.filter(id__gte=1).order_by('-id')
        s=""
        for q in qs:
            s+=str(q.store_url) + " : " + str(q.vid_url) + "\n"
        return s
