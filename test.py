from requests_html import AsyncHTMLSession
from dotenv import load_dotenv
import asyncio
import os

# Run functions to initialize ==================================================
load_dotenv()
assesion = AsyncHTMLSession()
# ==============================================================================

# Set the global variables =====================================================
YouTubeKey = os.environ["YouTubeKey"]
odoritora = "UCl79rcNN4Nxps7I0d-iXJpQ"
# ==============================================================================

def getVideoListURL(id):
    return f"https://jp.noxinfluencer.com/youtube/channel/{id}?tab=videos"

async def process(id):
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

    r = await assesion.get(getVideoListURL(id))
    await r.html.arender(keep_page=True)
    for _ in range(100):
        await loadMore(r)
        await asyncio.sleep(1)
    print(len(await getData(r)))

# Main =========================================================================
if __name__ == '__main__':
    id = odoritora
    assesion.run(lambda id=id: process(id))[0]
