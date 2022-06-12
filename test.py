from pyppeteer import launch
import asyncio
import time
import sys
import requests

def test(*args, **kargs):
    if args:
        print(*args, file=sys.stderr)
    if kargs:
        print(kargs, file=sys.stderr)

def printTime(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        test("{} seconds in {}".format(elapsed_time, func.__name__))
        return result
    return wrapper

async def main():
    def search(list):
        rtn = "https://twitter.com/search?q="
        for i, e in enumerate(list):
            rtn += e
            if i != len(list)- 1:
                rtn += " OR "
        rtn += "&src=typed_query&f=live"
        return rtn

    def getEmbedLink(url):
        return "https://publish.twitter.com/?query=" + url

    async def getData(page):
        script = """() =>{
            rtn = [];
            let arr = document.getElementsByClassName("css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0");
            for (let i = 0; i < arr.length; i++) {
                rtn.push(arr[i].href);
            }
            return {"data": rtn};
        }
        """

        return (await page.evaluate(script))["data"]

    async def waitForData(page):
        script = """() =>{
            let arr = document.getElementsByClassName("css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0");
            if(arr.length) return true;
        }
        """

        await page.waitForFunction(script)

    browser = await launch({
        "headless": True,
        'handleSIGINT': False,
        'handleSIGTERM': False,
        'handleSIGHUP': False
    }, args=["--no-sandbox"])
    page = await browser.newPage()
    await page.goto(search(["youtu.be/o3SFoyYY75w", "youtu.be/KGW1JNzxsIY", "https://youtu.be/KTnaCbRJ90c"]))
    await waitForData(page)
    rtn = await getData(page)
    #await page.screenshot({'path': 'example2.png', 'fullPage': True})
    await browser.close()
    return rtn

@printTime
def enter():
    test(asyncio.run(main()))

enter()