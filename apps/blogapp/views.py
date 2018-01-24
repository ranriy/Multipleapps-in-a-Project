from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "List of blogs"
	return HttpResponse(response)

def new(request):
	response = "Create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request, number):
	return HttpResponse("The number is" + number)

def edit(request, number):
	return HttpResponse("Edit number" + number)

def delet(request, number):
	return redirect('/')