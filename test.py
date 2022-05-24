from requests_html import HTMLSession
from dotenv import load_dotenv
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
    r.html.render()
    more = r.html.find("#btn-load-more-video", first = True)
    print(more)
    for e in r.html.find("#YouTube-Video-Wrap"):
        print(e.text)