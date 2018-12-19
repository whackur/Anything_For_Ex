#네이버 댓글 수집

import requests
import bs4
import pandas as pd

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=140652&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=%7B%7D%27'

count = 0
score_result = dict()

for page in range(0,3):
    res = requests.get(url.format(1))
    obj = bs4.BeautifulSoup(res.text,"html.parser")
    list2 = obj.find_all('div', {'class':'score_result'})[0].find_all('li')
    
    for li in list2:
        score_result[count] = {'score': int(li.em.text),
                              'reple' : li.p.text}
        count += 1

df = pd.DataFrame(score_result).T
df.to_csv('score_result.csv')


# 인코딩 변환
import codecs
 
infile = codecs.open('score_result.csv', 'r', encoding='utf-8')
outfile = codecs.open('score_result2.csv', 'w', encoding='euc_kr')
 
for line in infile:
     line = line.replace(u'\xa0', ' ')    # 가끔 \xa0 문자열로 인해 오류가 발생하므로 변환
     outfile.write(line)
 
infile.close()
outfile.close()