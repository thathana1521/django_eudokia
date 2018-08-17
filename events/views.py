from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from events.models import Event
import json

# Create your views here.

def getHomePage(request):
    return render(request, 'events/daily_events.html')

def get_all_events(request):
    events = Event.objects.all()
    jsonEvents = json.loads(serializers.serialize('json', events))
    return JsonResponse(jsonEvents, safe=False)
