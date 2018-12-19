import requests
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Request WebSite
host = 'https://www.boannews.com/media/t_list.asp'
html = urlopen(host)

#bs4
bsobj = BeautifulSoup(html.read(), 'html.parser')

#Find HyperLink
list_test = []
list_a = bsobj.findAll('a')
for a in list_a:
    if str(a).find('/media/view.asp') != -1:
        b = str(a).split('href="')[1]
        b = b.split('"')[0]
        list_test.append("https://www.boannews.com" + b)

#View
list_view = {}
for link in list(set(list_test))[:2]:
    html = urlopen(link).read()
    list_view[link] = html
    time.sleep(1)

import pandas as pd
df = pd.Series(list_view)
df