from ast import pattern
import enum
from pyppeteer import launch
from requests_html import AsyncHTMLSession
import time
import re

# Re Compiler ==================================================================
p = re.compile(r'https:\/\/www\.youtube\.com\/(watch\?v=|shorts\/)(.{11})')
# ============================================================================== 
# Set the global variables =====================================================
odoritora = "UCl79rcNN4Nxps7I0d-iXJpQ"
# ==============================================================================
async def getData(r):
    getDataScript = """
    () => {
        let arr = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer");
        rtn = [];
        for(let e of arr){
            rtn.push(e.href);
        }
        return {"data": rtn};
    }
    """
    return (await r.html.page.evaluate(getDataScript))["data"] 

async def loadMore(r):
    loadMoreScript = """
        async function(){
            const _sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
            let btn = document.querySelector("#btn-load-more-video");
            btn.click();
        }
        """ 
    await r.html.page.evaluate(loadMoreScript)

def getVideoListURL(id):
    return f"https://www.youtube.com/channel/{id}/videos"

def getVideoOriginalURL(temp : str):
    try:
        return p.match(temp).groups()[1]
    except:
        print(f"{temp} is not a valid URL")
        return -1

async def process(id=odoritora):
    assesion = AsyncHTMLSession()
    assesion.loop.set_debug(True)
    assesion._browser = await launch({
        'headless': True,
        'handleSIGINT': False,
        'handleSIGTERM': False,
        'handleSIGHUP': False
    }, args=["--no-sandbox"])
    r = await assesion.get(getVideoListURL(id))
    await r.html.arender(keep_page=True)
    #await r.html.page.screenshot({'path': './test.png', 'fullPage': True})
    rtn = await getData(r)
    for i, e in enumerate(rtn):
        rtn[i] = getVideoOriginalURL(e)
    await assesion.close()
    return rtn


