from requests_html import HTMLSession
from dotenv import load_dotenv
import importlib
import os

# Set the global variables =====================================================
load_dotenv()
YouTubeKey = os.environ["YouTubeKey"]
odoritora = "UCl79rcNN4Nxps7I0d-iXJpQ"
url = f"https://jp.noxinfluencer.com/youtube/channel/{odoritora}?tab=videos"
# ==============================================================================

# Main =========================================================================
if __name__ == '__main__':
    session = HTMLSession()
    r = session.get(url)
    script = """
       () => {
            const _sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
            let btn = document.querySelector("#btn-load-more-video");
            btn.click();
            await _sleep(2000);
            btn.click();
        }
        """ 
    r.html.render(script=script, scrolldown=10, sleep=0.1)
    print(len(r.html.find(".video-item")))
