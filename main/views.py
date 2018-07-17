from django.shortcuts import render

def index(request):
	return render(request, 'main/header.html')
	
def contact(request):
	return render(request, 'main/basic.html', {'content':['If you would like to contact me please email me.','athanthomas777@gmail.com']})