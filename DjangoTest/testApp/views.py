from django.shortcuts import render
from django.http import HttpResponse
from testApp.functions.debug import *
from testApp.classes.sessionInfo import sessionInfo
import json

sessionSet = {}

def index(request):
    return render(request, 'index.html')

@printTime
def form(request):
    sessionID = request.session.session_key
    id, numOfVideos= request.body.decode("utf-8").split("&")
    test(id, numOfVideos)
    if not sessionID:
        request.session.create()
    if not sessionID in sessionSet:
        sessionSet[sessionID] = sessionInfo()
    if sessionSet[sessionID].check():
        return HttpResponse(status=429)
    return HttpResponse(json.dumps(sessionSet[sessionID].getData(id, numOfVideos)))

@printTime
def add(request):
    sessionID = request.session.session_key
    return HttpResponse(json.dumps(sessionSet[sessionID].getData()))