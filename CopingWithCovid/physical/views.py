from django.shortcuts import render
from django.http import HttpResponse



def home(request):
	return render(request, 'physical/home.html', {'title': "Physical"})

def sleep(request):
	return render(request, 'physical/sleep.html', {'title': "Sleep"})

def exercise(request):
	return render(request, 'physical/exercise.html', {'title': "Exercise"})
