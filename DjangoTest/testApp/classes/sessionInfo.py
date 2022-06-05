from testApp.functions import functions as f
from pyppeteer import launch
import asyncio

class sessionInfo:
    # Variables ================================================================
    # id : str
    # page : pyppeteer.page.Page
    # loop : asyncio.events.AbstractEventLoop
    # ==========================================================================
    def __init__(self, id):
        async def initHelper(self):
            self.browser = await launch({
                'headless': True,
                'handleSIGINT': False,
                'handleSIGTERM': False,
                'handleSIGHUP': False
            }, args=["--no-sandbox"])
            self.page = await self.browser.newPage()

        self.id = id
        self.loop = asyncio.new_event_loop()
        self.loop.run_until_complete(initHelper(self))

    def getPage(self):
        async def getPageHelper(self):
            await self.page.goto(f.getVideoListURL(self.id))

        self.loop.run_until_complete(getPageHelper(self))

    def getData(self, numOfVideos):
        async def getDataHelper(self, numOfVideos):
            await f.waitForData(self.page, numOfVideos)
            return [f.getVideoOriginalURL(x) for x in await f.getData(self.page, numOfVideos)]

        return self.loop.run_until_complete(getDataHelper(self, numOfVideos))

    def check(self):
        return self.loop.is_running()

    def __del__(self):
        async def delHelper(self):
            await self.browser.close()

        self.loop.run_until_complete(delHelper(self))
        self.loop.close()