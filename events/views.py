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
    eventObjectList = []

    for e in events:
        today = datetime.now().date()        
        if e.day != today:
            eventObjectList.append(e)

    jsonEvents = json.loads(serializers.serialize('json', eventObjectList))
    return JsonResponse(jsonEvents, safe=False)
