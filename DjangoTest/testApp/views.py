from django.shortcuts import render
from django.http import HttpResponse
from requests import session
from testApp.functions.debug import *
from testApp.classes.sessionInfo import sessionInfo
import json

flagSetForTooManyRequests = {}
sessionSet = {}

def index(request):
    return render(request, 'index.html')

@printTime
def form(request):
    global flagSetForTooManyRequests, sessionSet
    sessionID = request.session.session_key
    if not sessionID:
        request.session.create()
        sessionID = request.session.session_key
    id = request.body.decode("utf-8").split("&")[0]
    seed = sessionID + id
    if not seed in sessionSet:
        sessionSet[seed] = sessionInfo()
    if seed in flagSetForTooManyRequests:
        return HttpResponse(status=429)
    flagSetForTooManyRequests[seed] = True
    rtn = HttpResponse(json.dumps(sessionSet[seed].getData(id)))
    flagSetForTooManyRequests.pop(seed)
    return rtn

@printTime
def add(request):
    sessionID = request.session.session_key
    id = request.body.decode("utf-8").split("&")[0]
    return HttpResponse(json.dumps(sessionSet[sessionID].getData(id)))