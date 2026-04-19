import random as rd

a = 0  #四星累積抽數
b = 0  #五星累積抽數
c = 0  #歪了之後必出限定


while True:
    gacha = eval(input("請選擇單抽(1)或10連抽(10)，輸入0以結束抽卡："))
    #選單抽或10抽
    if  gacha == 0:
        break
    elif gacha != 1 and gacha != 10:
        print("請輸入正確數字")
#抽卡機率設定
    rate1 = 0.006  #五星出貨率是0.6%
    rate2 = 0.051  #四星出貨率是5.1%

#單抽
    if gacha == 1:
        for i in range(0,1):
            n = rd.random()  #放迴圈內才會每次刷新亂數
            if a >= 7:
                rate2 = rate2 + 0.4715
            if b >= 74:
                rate1 = 0.006 + (b - 74) * 0.065  #逐漸增加五星機率直到第90抽時保底必出五星
            if 0 < n <= rate1:
                    n10 = rd.random()
                    if c == 1:
                        b = 0
                        c = 0
                        rate1 = 0.006
                        print('大保底：限定五星，當前機率：', rate1)
                    elif 0 <= n10 < 0.5:
                        c = 0
                        b = 0
                        rate1 = 0.006
                        print('小保底：限定五星，當前機率：', rate1)
                    elif 0.5 <= n10 <= 1:
                        n20 = rd.random()
                        if 0 <= n20 <= 0.05:
                            rate1 = 0.006    #重製機率
                            b = 0
                            c = 0
                            #重製保底抽數
                            # print('觸發特殊機制:捕獲明光')
                            print('捕獲明光：限定五星，當前機率：', rate1)
                        elif 0.05 < n20 < 1:
                            c = 1            #下一個出限定五星
                            rate1 = 0.006    #重製機率
                            b = 0
                            #重製保底抽數
                            print('保底歪：常駐五星，當前機率：', rate1)
            elif rate1 < n <= rate2: #第10抽時保底必出4星
                #出四星
                rate2 = rate1 + 0.015
                #重置機率
                a = 0
                #重置四星保底抽數
                b += 1
                #五星保底數+1
                print("四星，距離五星保底剩餘：", 90-b, "當前機率：", rate1)
            elif rate2 < n:
                a += 1  #四星保底計數+1
                b += 1  #五星保底計數+1
                print ("三星，距離五星保底剩餘：", 90-b, "當前機率：", rate1)

# 10 連抽
    if gacha == 10:
        for i in range(0,10):
            n = rd.random()  #放迴圈內才會每次刷新亂數
            if a >= 7:
                rate2 = rate2 + 0.4715
            if b >= 74:
                rate1 = 0.006 + (b - 74) * 0.065 #逐漸增加五星機率直到第90抽時保底必出五星
            if 0 < n <= rate1:
                n10 = rd.random()
                if c == 1:
                    b = 0
                    c = 0
                    rate1 = 0.006
                    print('大保底：限定五星，當前機率：', rate1)
                elif 0 <= n10 < 0.5:
                    c = 0
                    b = 0
                    rate1 = 0.006
                    print('小保底：限定五星，當前機率：', rate1)
                elif 0.5 <= n10 <= 1:
                    n20 = rd.random()
                    if 0 <= n20 <= 0.05:
                        rate1 = 0.006    #重製機率
                        b = 0
                        c = 0
                        #重製保底抽數
                        # print('觸發特殊機制:捕獲明光')
                        print('捕獲明光：限定五星，當前機率：', rate1)
                    elif 0.05 < n20 < 1:
                        c = 1            #下一個出限定五星
                        rate1 = 0.006    #重製機率
                        b = 0
                        #重製保底抽數
                        print('保底歪：常駐五星，當前機率：', rate1)
            elif rate1 < n <= rate2: #第10抽時保底必出4星
                #出四星
                rate2 = 0.051
                #重置機率
                a = 0
                #重置四星保底抽數
                b += 1
                #五星保底數+1
                print("四星，距離五星保底剩餘：", 90-b, "當前機率：", rate1)
            elif rate2 < n:
                a += 1  #四星保底計數+1
                b += 1  #五星保底計數+1
                print ("三星，距離五星保底剩餘：", 90-b, "當前機率：", rate1)

    




