import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

#print(bsObj.find("div", {"class":"area_navigation"}))
menu = (bsObj.find("div", {"class":"area_navigation"}))


#menu_link = (menu.find("li",{"class":"an_item"}))
menu_link = (menu.find_all("li",{"class":"an_item"}))

print(menu_link)