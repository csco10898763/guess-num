# 產生一個隨機整數 1 ~ 100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案 大 / 小

import random
i = 0 
x = 0
y = 0
x = int(input('請輸入起始數字：'))
y = int(input('請輸入結束數字：'))   
r = random.randint(x, y)

while True:
    i = i + 1
    num = input('請猜數字：')
    num = int(num)
    if num == r: 
        print('您猜了有', i, '次')
        print('\n終於猜對了 !!!')
        break
    elif num > r:
        print('\n請猜小一點 !!!')
    elif num < r:
        print('\n請猜大一點 !!!')
