import asyncio

async def getSearchResult(list, browser):
    def search(list):
        rtn = "https://twitter.com/search?q="
        for i, e in enumerate(list):
            rtn += "youtu.be/" + e
            if i != len(list)- 1:
                rtn += " OR "
        rtn += "&src=typed_query&f=live"
        return rtn

    async def getData(page):
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
        flagSet = {}
        rtn = []
        while 1:
            prevLength = len(flagSet)
            list = (await page.evaluate(script))["data"]
            for e in list:
                if e in flagSet:
                    continue
                flagSet[e] = True
                rtn.append(e)
            if prevLength == len(rtn):
                break
        return rtn

    async def waitForData(page):
        script = """() =>{
            let arr = document.getElementsByClassName("css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0");
            if(arr.length) return true;
        }
        """
        await page.waitForFunction(script)

    async def enter(partOfList, browser):
        page = await browser.newPage()
        await page.goto(search(partOfList))
        await waitForData(page)
        rtn = await getData(page)
        await page.close()
        return rtn

    tasks = [enter(list[i: i + 5], browser) for i in range(0, len(list), 5)]
    rtn = await asyncio.gather(*tasks)
    return [e + "?ref_src=twsrc%5Etfw" for temp in rtn for e in temp]