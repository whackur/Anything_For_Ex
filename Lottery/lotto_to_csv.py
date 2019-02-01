import csv
from random import shuffle

lotto = []
repeat = 1000

with open("numbers.csv", "w", newline='') as f:
    for r in range(repeat):
        for i in range(1,46):
            lotto.append(i)
        shuffle(lotto)
        
        ### 6개의 당첨번호와 1개의 보너스 번호
        #lotto = lotto[:7] 
        
        # 6개의 당첨번호
        lotto = lotto[:6] 
        print(lotto)
        writer = csv.writer(f)
        writer.writerow(lotto)