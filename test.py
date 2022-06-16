from pyppeteer import launch
import asyncio
import time
import sys
async def getSearchResult():
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

    async def getData(page, resultSet):
        script = """() =>{
            rtn = [];
            let arr = document.getElementsByClassName("css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0");
            for (let i = 0; i < arr.length; i++) {
                rtn.push(arr[i].href);
            }
            arr[arr.length - 1].scrollIntoView();
            return {"data": rtn};
        }
        """

        resultSet |= set((await page.evaluate(script))["data"])

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
    resultSet = set()
    await waitForData(page)
    while 1:
        prevLength = len(resultSet)
        await getData(page, resultSet)
        if prevLength == len(resultSet):
            break
    await browser.close()
    return resultSet
