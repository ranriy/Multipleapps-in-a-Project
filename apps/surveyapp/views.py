from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def display(request):
	return HttpResponse("Display all surveys")

def new(request):
	return HttpResponse("Add a new survey")

