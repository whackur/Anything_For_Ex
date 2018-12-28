#순차적으로 데이터 선택하여 출력해보기
import bs4

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
        <div>
            <ul>
                <li>open</li>
                <li>close</li>
            </ul>
        </div>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

lis = bs_obj.findAll("li")

#bye 텍스트 뽑기
print(lis[1].text)

#div 안의 li 줄의 텍스트 open, close 뽑기
div = bs_obj.find("div")
div_li = div.findAll("li")

for li in div_li:
    print(li.text)