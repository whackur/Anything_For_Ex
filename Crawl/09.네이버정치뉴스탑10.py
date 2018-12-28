#네이버정치뉴스탑10
from urllib.request import urlopen
import bs4

url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")

ul = bs_obj.find("ul",{"class":"section_list_ranking"})

lis = ul.findAll("li")

titles = [li.text for li in lis]

print("정치 Top10")
print("=================================================")
for title in titles:
    print(title)