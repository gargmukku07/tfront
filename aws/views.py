from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

#def index(request):
#	return HttpResponse("My Name is Mukul")

def index(request):
	return render(request, "index.html", {})

def login(request):
	return render(request, "login.html", {})

def logout(request):
	return render(request, "logout.html", {})

def hello(request):
	return render(request, "hello.html", {})
