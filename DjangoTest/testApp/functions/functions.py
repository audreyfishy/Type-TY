from requests_html import AsyncHTMLSession

# Run functions to initialize ==================================================
assesion = AsyncHTMLSession()
# ==============================================================================

# Set the global variables =====================================================
odoritora = "UCl79rcNN4Nxps7I0d-iXJpQ"
# ==============================================================================

def main(id):
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
        def getVideoListURL(id):
            return f"https://jp.noxinfluencer.com/youtube/channel/{id}?tab=videos"
        r = await assesion.get(getVideoListURL(id))
        await r.html.arender(keep_page=True)
        return await getData(r)
    return assesion.run(lambda id=id: process(id))[0]


