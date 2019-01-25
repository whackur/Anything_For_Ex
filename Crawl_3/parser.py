import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
# CSS Selector를 통해 html요소들을 찾아낸다.

my_titles = soup.select(
  'h3 > a'
)

for title in my_titles:
    ## Tag안의 텍스트
    print(title.text,end='\n')
    ## Tag의 속성을 가져오기(ex: href속성)
    #print(title.get('href'))