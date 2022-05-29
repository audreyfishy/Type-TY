import requests as r
from bs4 import BeautifulSoup as bs
res = r.get("https://www.youtube.com/results?search_query=content&sp=EgIQAg%253D%253D")
soup = bs(res.content, "html.parser")
print(soup.select("#text-container"))