from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from room.models import Room

urlpatterns= [
	url(r'^$', ListView.as_view(queryset=Room.objects.all().order_by("id")[:10],template_name="room/rooms.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Room, template_name='room/room.html'))]