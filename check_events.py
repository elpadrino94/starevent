import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from events.models import Event

events = Event.objects.all()
print(f'Number of events: {events.count()}')
for e in events:
    print(f'Event: {e.title}, Image: {e.image}, URL: {e.image.url if e.image else "No image"}')