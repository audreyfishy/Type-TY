from curses.ascii import NUL
from requests_html import AsyncHTMLSession

# Run functions to initialize ==================================================

# ==============================================================================

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
    print("--- Start ---")
    assesion = AsyncHTMLSession()
    print("--- Get URL ---")
    r = await assesion.get(getVideoListURL(id))
    print("--- Get Data ---")
    await r.html.arender(keep_page=True)
    print("--- Get Yeah ---")
    rtn = await getData(r)
    print("___ Get More ___")
    await assesion.close()
    print("done------")
    return rtn


