import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cache_server.settings')
django.setup()
from cache_video.models import TrackingUrl, LocalUrl, UploadedFile
print(TrackingUrl.objects.all()[1].subject)


f = open('tmp_data.csv', 'r')
info = []
rdr = csv.reader(f)
tracking_url = TrackingUrl.objects.get(url='https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA')
for row in rdr:
    subject, thumbnail, url, running_time = row
    local = " "
    db = LocalUrl(tracking_url=tracking_url, subject=subject, thumbnail=thumbnail, local=local, url=url, running_time=running_time)
    db.save()
