#네이버 주요 뉴스 파싱
from urllib.request import urlopen
import bs4

url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")

ul = bs_obj.find("ul",{"id":"text_today_main_news_801001"})

lis = ul.findAll("li")

titles = [li.find("strong").text for li in lis]

for title in titles:
    print(title)
    
'''
for li in lis:
    strong = li.find("strong")
    print(strong.text)
'''