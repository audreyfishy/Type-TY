import re

# Re Compiler ==================================================================
p = re.compile(r'https:\/\/www\.youtube\.com\/(watch\?v=|shorts\/)(.{11})')
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
            window.scrollBy(0, 10000);
        }
        """ 
    await r.html.page.evaluate(loadMoreScript)
    return r

def getVideoListURL(id):
    return f"https://www.youtube.com/channel/{id}/videos"

def getVideoOriginalURL(temp : str):
    try:
        return p.match(temp).groups()[1]
    except:
        print(f"{temp} is not a valid URL")
        return -1


