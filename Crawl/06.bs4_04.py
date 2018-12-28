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

#ok no sure 텍스트뽑기
ul_reply = bs_obj.find("ul",{"class":"reply"})

lis = ul_reply.findAll("li")

for li in lis:
    print(li.text)