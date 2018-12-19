import requests

url = 'https://www.boannews.com/media/t_list.asp'
res = requests.get(url)

print(res)
print(res.status_code)
print(res.content[:1024])