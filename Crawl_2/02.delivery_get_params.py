import requests

url = 'https://www.boannews.com/media/view.asp'
my_params = {
    'idx' : '10000'
}

res = requests.get(url, my_params)

print(res)
print(res.content[:1024])