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
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

lis = bs_obj.findAll("li")
print(lis)

for li in lis:
    print(li)