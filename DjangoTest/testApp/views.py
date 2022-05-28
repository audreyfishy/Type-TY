from django.shortcuts import render
from django.http import HttpResponse
from testApp.functions import functions as f
import asyncio as a
import json
def index(request):
    return render(request, 'index.html')

def form(request):
    id = request.body.decode("utf-8")
    return HttpResponse(json.dumps(a.run(f.process(id))))
