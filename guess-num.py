# 產生一個隨機整數 1 ~ 100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案 大 / 小

import random
count = 0 
x = 0
y = 0
x = int(input('請輸入起始數字：'))
y = int(input('請輸入結束數字：'))   
r = random.randint(x, y)

while True:
    count += 1 # count = count + 1
    num = int(input('\n請猜數字：'))
    print('\n這是你的猜第', count, '次')
    
    if num == r: 
        print('\n終於猜對了 !!!')
        break
    elif num > r:
        print('\n請猜小一點 !!!')
    elif num < r:
        print('\n請猜大一點 !!!')
