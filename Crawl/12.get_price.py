import requests
from bs4 import BeautifulSoup

#url을 넣어서 bs_obj를 return하는 function
def get_bs_obj(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

#company_code를 받아서 price return
def get_price(company_code):
    url = "https://finance.naver.com/item/main.nhn?code="+company_code
    bs_obj = get_bs_obj(url)
    no_today = bs_obj.find("p",{"class":"no_today"})
    blind = no_today.find("span",{"class":"blind"})
    return blind.text

#삼성, SK하이닉스, 삼영
company_codes = ["005930","000660","005680"]

for item in company_codes:
    price = get_price(item)
    print(price)