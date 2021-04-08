from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'physical/home.html', {'title': "Home"})

def sleep(request):
	return render(request, 'physical/sleep.html', {'title': "Sleep"})

def exercise(request):
	return render(request, 'physical/exercise.html', {'title': "Exercise"})
