#from django.shortcuts import render
from django.http import HttpResponse

from .models import Employee

def index(request):
	return HttpResponse('Hello, World')
