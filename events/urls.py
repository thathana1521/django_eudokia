from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from events.models import Event

urlpatterns= [
	url(r'^$', ListView.as_view(queryset=Event.objects.all().order_by("id")[:10],template_name="events/daily_events.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Event, template_name='events/event.html'))]