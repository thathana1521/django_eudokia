from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from events.models import Event
from events.views import get_all_events, getHomePage

urlpatterns= [
	url(r'^$', getHomePage),
	url(r'^get-all-events', get_all_events),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Event, template_name='events/index.html'))]