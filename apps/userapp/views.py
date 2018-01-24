from django.shortcuts import render,  redirect, HttpResponse

# Create your views here.
def register(request):
	return HttpResponse('Create a new record')

def login(request):
	return HttpResponse('Login')

def display(request):
	return HttpResponse("Display all users")