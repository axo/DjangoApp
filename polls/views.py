# Create your views here.
#from django.template import Context, loader
#from django.http import HttpResponse
#from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render_to_response
from polls.models import Poll


def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	# Old code
	#t = loader.get_template('polls/index.html')
	#c = Context({
	#	'latest_poll_list': latest_poll_list,
	#})
	#return HttpResponse(t.render(c))
	# Same thing rewritten
	return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
	#return HttpResponse("You're looking at poll %s." % poll_id)
	# Old code
	#try:
	#	p = Poll.objects.get(pk=poll_id)
	#except Poll.DoesNotExist:
	#	raise Http404
	#return render_to_response('polls/detail.html', {'poll': p})
	# Samed thin rewritten
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/detail.html', {'poll': p})

def results(request, poll_id):
	#return HttpResponse("You're looking at the results of poll %s." % poll_id)
	return render_to_response('polls/results.html', {'poll_id': poll_id})

def vote(request, poll_id):
	#return HttpResponse("You're voting on poll %s." % poll_id)
	return render_to_response('polls/vote.html', {'poll_id': poll_id})

