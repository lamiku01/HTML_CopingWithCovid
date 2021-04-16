from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, 'users/home.html', {'title': "Home"})

def login(request):
	return render(request, 'users/login.html', {'title': "Home"})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created for {username}!')
			return redirect('users/home.html')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})

