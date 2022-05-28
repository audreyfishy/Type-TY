from django.shortcuts import render
from django.http import HttpResponse
from testApp.functions import functions as f
import asyncio as a

def index(request):
    return render(request, 'index.html')

def form(request):
    a.run(f.process())
    return HttpResponse()
