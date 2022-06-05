import re

# Re Compiler ==================================================================
p = re.compile(r'https:\/\/www\.youtube\.com\/(watch\?v=|shorts\/)(.{11})')
# ==============================================================================

async def getData(page, num):
    getDataScript = """() =>{
        let arr = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer");
        rtn = [];
        count = 0;
        for(let e of arr){
            if(count >= """+num+""")
                break;
            rtn.push(e.href);
            count++;
        }
        return {"data": rtn};
    }
    """
    return (await page.evaluate(getDataScript))["data"]

async def waitForData(page, num):
    await page.waitForFunction("""() => {
        if(document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer").length > """+num+""")
            return true;
        arr = document.getElementsByClassName("style-scope ytd-message-renderer");
        for(let e of arr){
            try{
                if(e.id == "message")
                    return true;
            }
            catch(e){
                continue;
            }
        }
        window.scrollBy(0, 10000);
        return false;
    }
    """)

async def loadMore(page):
    loadMoreScript = """
        function(){
            window.scrollBy(0, 10000);
        }
        """
    await page.evaluate(loadMoreScript)

def getVideoListURL(id):
    return f"https://www.youtube.com/channel/{id}/videos"

def getVideoOriginalURL(temp : str):
    try:
        return p.match(temp).groups()[1]
    except:
        print(f"{temp} is not a valid URL")
        return -1


