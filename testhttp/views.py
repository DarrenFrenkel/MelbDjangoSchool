from django.http import HttpResponse

def get_request(request):
	if request.method == 'GET':
		html = "This is my httpresponse"
		return HttpResponse(html)

# views.py file
