from django.shortcuts import render
from pyppeteer import launch
from django.http import HttpResponse
from requests_html import AsyncHTMLSession
from testApp.functions import functions as f
from testApp.functions import debug as d
import asyncio
import json

sessionSet = {}

class sessionInfo:
    def __init__(self, id):
        async def initHelper(self):
            self.assesion = AsyncHTMLSession()
            self.assesion._browser = await launch({
                'headless': True,
                'handleSIGINT': False,
                'handleSIGTERM': False,
                'handleSIGHUP': False
            }, args=["--no-sandbox"])
            self.r = await self.assesion.get(f.getVideoListURL(self.id))
            await self.r.html.arender(keep_page=True)

        self.id = id
        self.loop = asyncio.new_event_loop()
        self.loop.run_until_complete(initHelper(self))

    def getData(self):
        async def getDataHelper(self):
            return [f.getVideoOriginalURL(x) for x in await f.getData(self.r)]
        return self.loop.run_until_complete(getDataHelper(self))

    def __del__(self):
        async def delHelper(self):
            await self.assesion.close()

        self.loop.run_until_complete(delHelper(self))
        self.loop.close()
        
def index(request):
    return render(request, 'index.html')

@d.printTime
def form(request):
    if not request.session.session_key:
        request.session.create() 
    sessionID = request.session.session_key
    sessionSet[sessionID] = sessionInfo(request.body.decode("utf-8"))
    return HttpResponse(json.dumps(sessionSet[sessionID].getData()))

@d.printTime
def add(request):
    sessionID = request.session.session_key
    return HttpResponse(json.dumps(sessionSet[sessionID].getData()))