from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
import numpy as np
from django.shortcuts import render
from django.template import loader

# Create your views here.
# def index(request):
# 	all_events = Events.objects.all()
# 	html = ''
# 	for event in all_events:
# 		url = '/history/'+ str(event.id) +'/'
# 		html+= '<a href="' + url + '">' + event.place + '</a><br>' 
#   return HttpResponse(html)

def index(request):
	all_events = Events.objects.all()
	template = loader.get_template('history/index.html')
	context = {'all_events': all_events}	
	# return HttpResponse(template.render(context, request))
	return render(request, 'history/index.html', context)


def detail(request, event_id):
	str_val = "<h2> Your requested event " +str(event_id) + " is here </h2>"
	return HttpResponse(str_val)