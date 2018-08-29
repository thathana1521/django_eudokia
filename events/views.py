from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from events.models import Event
import json
from datetime import datetime

# Create your views here.

def getHomePage(request):
    return render(request, 'events/daily_events.html')

def get_all_events(request):
    events = Event.objects.all()
    
    for e in events:
        today = datetime.now().date()
        print (today)
        print (e.day)
        if e.day == today:
            e.delete()

    jsonEvents = json.loads(serializers.serialize('json', events))
    return JsonResponse(jsonEvents, safe=False)
