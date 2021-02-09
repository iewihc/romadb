
def JinFish(currentPrice):
    zeny = 6300
    energy = 10
    P = 0.7

    zenyTotal = 2000 / energy * zeny
    afterTax = currentPrice * 0.9
    CP = (200*P*currentPrice*0.9 ) / 2000

    print(f"燼魚: ZENY : {zenyTotal} , 稅後價: {afterTax} , CP: {CP} ")

def Goldflower(currentPrice):
    energy = 20
    zeny = 0
    afterTax = currentPrice * 0.9
    print(f"黃金花: ZENY: {zeny} , 稅後價: {afterTax} , CP:{afterTax/20}")
def Mining(currentPrice):
    強化金屬LV1 = 538 * 133
    煤礦石LV1 = 153 * 50
    精魔礦石LV1 = 183 * 42
    魔力之石礦石LV1 = 18 * 946
    神之金屬礦石LV1 = 37 * 1280
    Total = 強化金屬LV1+煤礦石LV1+精魔礦石LV1+魔力之石礦石LV1+神之金屬礦石LV1
    print(f"挖礦: ZENY: {270000} , 稅後價:{Total*0.9} , CP:{Total*0.9/2000}")


JinFish(1530)
Goldflower(2420)
Mining(2)