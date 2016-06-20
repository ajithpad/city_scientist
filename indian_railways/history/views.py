from django.shortcuts import render
from django.http import HttpResponse
from .models import Events, Stories
import numpy as np
from django.shortcuts import render, get_object_or_404
from django.template import loader
import pickle
from django.http import Http404

# Create your views here.
# def index(request):
# 	all_events = Events.objects.all()
# 	html = ''
# 	for event in all_events:
# 		url = '/history/'+ str(event.id) +'/'
# 		html+= '<a href="' + url + '">' + event.place + '</a><br>' 
#   return HttpResponse(html)
df = pickle.load(open("non_zero_codes.p","rb"))
def index(request):
	all_events = Events.objects.all()
	template = loader.get_template('history/index.html')
	context = {'all_events': all_events}	
	# return HttpResponse(template.render(context, request))
	return render(request, 'history/index.html', context)


# def detail(request, event_id):
# 	try:
# 		event = Events.objects.get(pk = event_id)
# 	except Events.DoesNotExist:
# 		raise Http404("Event does not exist")
# 	return render(request, 'history/detail.html', {'event':event})

def detail(request, event_id):
	event = get_object_or_404(Events, pk = event_id)
	return render(request, 'history/detail.html', {'event':event})

def favorite(request, event_id):
	event = get_object_or_404(Events, pk = event_id)
	try:
		selected_story = Stories.objects.get(pk= request.POST['story'])
	except (KeyError, Stories.DoesNotExist):
		return render(request, 'history/detail.html', {'event':event, 'error_message' : "You did not select a valid story",})
	else:
		selected_story.is_favorite = True
		selected_story.save()
		return render(request, 'history/detail.html', {'event':event})