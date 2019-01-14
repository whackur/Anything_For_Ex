import requests
from urllib.parse import quote

def get1000Result(keyword):
    list = []
    for num in range(0,10):
        list = list + call("keyword",num*100 + 1)['items']
    return list

def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=100"+"&start="+str(start)
    result = requests.get(url=url,
        headers={"X-Naver-Client-Id":"0lg2EGVNjq6YXABdu32J",
            "X-Naver-Client-Secret":"LtSN06zSRs"})
    print(result)
    return result.json()