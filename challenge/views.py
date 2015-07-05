from django.http import HttpResponse
import json
from challenge.models import Challenge
from django.contrib.auth.models import User

def add(request):
	challenge_request = json.loads(request.body)

	challenge = Challenge(
		title = challenge_request['title'],
		frequency = challenge_request['frequency'],
		startdate = challenge_request['startdate'][0:10],
		numberofdays = challenge_request['numberofdays']
		)

	challenge.save()

	for challenger in challenge_request['friends']:
		challenge.challengers.add(User.objects.get(pk = challenger['pk']))
	
	return HttpResponse()

def list(request):

	challenge_list = Challenge.objects.all()

	data = []
	for challenge in challenge_list:
		data.append({
			"title":challenge.title,
			"frequency":challenge.frequency,
			"startdate":challenge.startdate.isoformat(),
			"numberofdays":challenge.numberofdays
			})

	return HttpResponse(json.dumps(data))

def user_list(request):

	user_list = User.objects.all()

	data = []
	for user in user_list:
		data.append({
			"username":user.username,
			"first_name":user.first_name,
			"last_name":user.last_name,
			"email":user.email,
			"pk":user.pk
			})

	return HttpResponse(json.dumps(data))


