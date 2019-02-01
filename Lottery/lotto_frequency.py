import pandas as pd

number = pd.read_csv('numbers.csv', names=['N1','N2','N3','N4','N5','N6','Bonus'])

### 모든 테이블 출력
# print(number)

### 보너스 당첨 번호별 빈도
print(number['Bonus'].value_counts())

### 당첨 번호별 정렬
print(number.apply(pd.value_counts))
