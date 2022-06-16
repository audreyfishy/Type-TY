import re
from socket import timeout
from testApp.functions.debug import *
from testApp.classes.video import Video

async def getData(page, num, result):
    lengthOfList = str(len(result))
    getDataScript = """() =>{
        let arr = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer");
        rtn = [];
        for(let i = """+lengthOfList+"""; i < arr.length && i < """+str(num)+"""; i++)
            rtn.push(arr[i].href);
        return {"data": rtn};
    }
    """
    result.extend(list(map(getVideo, (await page.evaluate(getDataScript))["data"])))
    return result

async def waitForData(page, num, result):
    if not result:
        await page.waitForFunction("""() => {
            var elm = document.documentElement;
            var currentHeight = elm.scrollHeight;
            var bottom = currentHeight - elm.clientHeight;
            window.scroll(0, bottom);
            if(document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer").length)
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
            arr = document.getElementsByClassName("ERROR style-scope yt-alert-renderer");
            for(let e of arr){
                try{
                    if(e.id == "container")
                        return true;
                }
                catch(e){
                    continue;
                }
            }
            return false;
        }
        """)
    else:
        await page.waitForFunction("""() => {
            var elm = document.documentElement;
            var currentHeight = elm.scrollHeight;
            var bottom = currentHeight - elm.clientHeight;
            window.scroll(0, bottom);
            if(document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer").length > """+str(num)+""")
                return true;
            if(currentHeight === document.documentElement.scrollHeight)
                return true;
            return false;
        }
        """, timeout=3000)

def getVideoListURL(id):
    return f"https://www.youtube.com/channel/{id}/videos"

def getVideo(temp : str):
    p = re.compile(r'https:\/\/www\.youtube\.com\/(watch\?v=|shorts\/)(.{11})')
    try:
        return Video(p.match(temp).groups()[1]).toString()
    except:
        print(f"{temp} is not a valid URL")
        return -1


