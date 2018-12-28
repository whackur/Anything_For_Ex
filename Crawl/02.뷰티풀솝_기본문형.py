#pip install bs4
import bs4

html_str = "<html><head>This is Head</head><div>Something In Here</div/></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
print(bsObj.find("head"))