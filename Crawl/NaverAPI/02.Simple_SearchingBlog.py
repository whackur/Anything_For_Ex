#좀 더 간단한 형식으로 코드 수정

import requests
from urllib.parse import urlparse

keyword = "정보보안"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(), 
    headers={"X-Naver-Client-Id":"0lg2EGVNjq6YXABdu32J",
            "X-Naver-Client-Secret":"LtSN06zSRs"})

json_obj = result.json()
print(json_obj)