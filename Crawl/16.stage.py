from gn_lib3.naver_api_caller import get1000Result
import json

list = []
result = get1000Result("강남역 맛집")
result2 = get1000Result("강남역 카페")
list = list + result + result2

file = open("./gangnam.json","w+")
file.write(json.dumps(list))