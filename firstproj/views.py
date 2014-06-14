from django.http import HttpResponse
import datetime

def main(request):
	return HttpResponse("Welcome home")

def time(request):
	now = datetime.datetime.now()
	html = "<html><body>Current time is %s.</body></html>" % now
	return HttpResponse(html)

