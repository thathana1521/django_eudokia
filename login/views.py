from django.shortcuts import render

def index(request):
	return render(request, 'login/login_and_registration.html')