from django.shortcuts import render
from django.http import HttpResponse
from testApp.functions import debug as d
from testApp.classes.sessionInfo import sessionInfo
import json

sessionSet = {}

def index(request):
    return render(request, 'index.html')

@d.printTime
def form(request):
    sessionID = request.session.session_key
    id, numOfVideos= request.body.decode("utf-8").split("&")
    print(id, numOfVideos, sessionID)
    if not sessionID:
        request.session.create()
    if not sessionID in sessionSet:
        sessionSet[sessionID] = sessionInfo(id)
    if sessionSet[sessionID].check():
        return HttpResponse(status=429)
    sessionSet[sessionID].getPage()
    return HttpResponse(json.dumps(sessionSet[sessionID].getData(numOfVideos)))

@d.printTime
def add(request):
    sessionID = request.session.session_key
    return HttpResponse(json.dumps(sessionSet[sessionID].getData()))