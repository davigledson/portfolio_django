from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return render(request, 'home_page/index.html')


def resume(request):
	return render(request, 'home_page/resume.html')