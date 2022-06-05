import asyncio
from multiprocessing.connection import wait
import time

def waitForData(num):
    print(("""() => {
        if(document.getElementsByClassName("yt-simple-endpoint style-scope ytd-grid-video-renderer").length > {0})
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
    """.format(num)))

waitForData(10)