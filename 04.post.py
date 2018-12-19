import requests, json

host = 'https://www.boannews.com/'

myData = json.dumps({'id':'gasbugs', 'pw':'passwords'})
myCookie = { 'ASPSESSIONIDAACQTCSS' : 'OLHIMDDBBKMJCNIHALLOFFHC', 'dable_uid' : '79705445.1544715327374' }
myHeaders = { 'User-Agent' : 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0' }
res = requests.post(host, data = myData, headers = myHeaders, cookies = myCookie)

print(res.content[:1024])