from django.shortcuts import render
from django.http import HttpResponse
from testApp.functions import functions as f
import asyncio as a
import json
import time
def index(request):
    return render(request, 'index.html')

def form(request):
    currentTime = time.time()
    id = request.body.decode("utf-8")
    rtn = HttpResponse(json.dumps(a.run(f.process(id))))
    print(time.time() - currentTime)
    return rtn