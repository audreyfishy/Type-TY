from testApp.functions import functions as f
from testApp.classes.video import Video
from pyppeteer import launch
import asyncio

class sessionInfo:
    # Variables ================================================================
    # id : str
    # result : list
    # page : pyppeteer.page.Page
    # loop : asyncio.events.AbstractEventLoop
    # ==========================================================================
    def __init__(self):
        async def initHelper(self):
            self.browser = await launch({
                'headless': True,
                'handleSIGINT': False,
                'handleSIGTERM': False,
                'handleSIGHUP': False
            }, args=["--no-sandbox"])
            self.page = await self.browser.newPage()

        self.id = ""
        self.loop = asyncio.new_event_loop()
        self.loop.run_until_complete(initHelper(self))

    def getPage(self, id=""):
        async def getPageHelper(self):
            await self.page.goto(f.getVideoListURL(self.id))

        if id == self.id:
            return
        self.id = id
        self.result = []
        self.loop.run_until_complete(getPageHelper(self))

    def getData(self, id, numOfVideos):
        async def getDataHelper(self, numOfVideos):
            await f.waitForData(self.page, numOfVideos, self.result)
            return await f.getData(self.page, numOfVideos, self.result)

        self.getPage(id)
        return self.loop.run_until_complete(getDataHelper(self, numOfVideos))

    def check(self):
        return self.loop.is_running()

    def __del__(self):
        async def delHelper(self):
            await self.browser.close()

        self.loop.run_until_complete(delHelper(self))
        self.loop.close()