#시고저종 캔들차트 데이터 가져오기
#findAll 예제 배우기 전
import requests
from bs4 import BeautifulSoup

#url을 넣어서 bs_obj를 return하는 function
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code="+company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

#company_code를 받아서 price return
def get_candle_chart_data(company_code):   
    bs_obj = get_bs_obj(company_code)
    td_first = bs_obj.find("td",{"class":"first"})
    blind = td_first.find("span",{"class":"blind"})

    #close 전일 종가
    close = blind.text
    
    #high 고가
    table = bs_obj.find("table",{"class":"no_info"})
    trs = table.findAll("tr")
    first_tr = trs[0]
    first_tr_tds = first_tr.findAll("td")
    first_tr_tds_second_td = first_tr_tds[1]
    
    
    high = first_tr_tds_second_td.find("span",{"class":"blind"}).text


    return {"close":close,"high":high}


#sk하이닉스 000660
candle_chart_data = get_candle_chart_data("000660")
print(candle_chart_data)