from pyppeteer import launch
from requests_html import AsyncHTMLSession

# Set the global variables =====================================================
odoritora = "UCl79rcNN4Nxps7I0d-iXJpQ"
# ==============================================================================

async def process(id=odoritora):
    async def getData(r):
        getDataScript = """
        () => {
            let arr = document.getElementsByClassName("video-item");
            rtn = [];
            for(let e of arr){
                rtn.push(e.childNodes[0].getAttribute("data-video-id"));
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
        return f"https://jp.noxinfluencer.com/youtube/channel/{id}?tab=videos"
    assesion = AsyncHTMLSession()
    assesion._browser = await launch({
        'ignoreHTTPSErrors': True,
        'headless': True,
        'handleSIGINT': False,
        'handleSIGTERM': False,
        'handleSIGHUP': False
    }, args=["--no-sandbox"])
    r = await assesion.get(getVideoListURL(id))
    await r.html.arender(keep_page=True, timeout = 10, sleep=0.1, wait=0.1)
    rtn = await getData(r)
    await assesion.close()
    return rtn


