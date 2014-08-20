from django.shortcuts import render
from django.http import HttpResponse

def get_request(request):
	if request.method == 'POST':
		html = "This is my httpresponse"
		return HttpResponse(html)
