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
    rate2 = rate1 + 0.045  #四星出貨率是5.1%(就是0.6%+4.5%)
    
#單抽
    if gacha == 1:
        n = rd.random()  #放迴圈內才會每次刷新亂數
        if a >= 7:
            rate2 = rate2 + 0.4745
        if b >= 73:
            rate1 += 0.06  #逐漸增加五星機率直到第90抽時保底必出五星
        if 0 < n <= rate1:
            n1 = rd.random()
            if c == 1:
                print('限定五星')
            elif c == 0:
                if 0 < n1 < 0.5:
                    print('限定五星')
                    c = 0
                    rate1 = 0.006
                    #重製機率
                    a = 0
                    b = 0
                    #重製保底抽數
                elif 0.5 <= n1 <= 1:
                    n2 = rd.random()
                    if 0 <= n2 <= 0.05:
                        print('觸發特殊機制:捕獲明光')
                        print('限定五星')
                        c = 0
                        rate1 = 0.006
                        #重製機率
                        a = 0
                        b = 0
                        #重製保底抽數
                    else:
                        print('常駐五星')
                        c = 1
                        rate1 = 0.006
                        #重製機率
                        a = 0
                        b = 0
                        #重製保底抽數
        elif rate1 < n <= rate2: #第10抽時保底必出4星
            print("四星")
            #出四星
            rate2 = rate1 + 0.045
            #重置機率
            a = 0
            #重置四星保底抽數
            b += 1
            #五星保底數+1
        elif rate2 < n:
            print ("三星")
# 10 連抽
    if gacha == 10:
        for i in range(0,10):
            n = rd.random()  #放迴圈內才會每次刷新亂數
            if a >= 7:
                rate2 = rate2 + 0.4745
            if b >= 73:
                rate1 += 0.06  #逐漸增加五星機率直到第90抽時保底必出五星
            if 0 < n <= rate1:
                n10 = rd.random()
                if 0 < n10 < 0.5:
                    print('限定五星')
                    c = 0
                elif 0.5 <= n10 <= 1:
                    n20 = rd.random()
                    if 0 <= n20 <= 0.05:
                        print('觸發特殊機制:捕獲明光')
                        print('限定五星')
                        c = 0
                        rate1 = 0.006    #重製機率
                        a = 0
                        b = 0
                        #重製保底抽數
                    else:
                        print('常駐五星')
                        c = 1
                        #出五星
                        rate1 = 0.006    #重製機率
                        a = 0
                        b = 0
                        #重製保底抽數
            elif rate1 < n <= rate2: #第10抽時保底必出4星
                print("四星")
                #出四星
                rate2 = rate1 + 0.045
                #重置機率
                a = 0
                #重置四星保底抽數
                b += 1
                #五星保底數+1
            elif rate2 < n:
                print ("三星")
                a += 1  #四星保底計數+1
                b += 1  #五星保底計數+1
    




