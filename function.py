import time,datetime


h=int(datetime.datetime.now().strftime('%H'))
print(h)
def avg_do(maxDaily,minDaily):
    deltaDay=round((maxDaily-minDaily)/8,1)
    deltaNight=round((maxDaily-minDaily)/16,1)
    if h<14 and h>5:
        minHour=minDaily+(deltaDay*(h-6))
        maxHour=minDaily+(deltaDay*(h-6)+deltaDay)
    elif h>13:
        minHour=maxDaily-(deltaNight*(h-14)+deltaNight)
        maxHour=maxDaily-(deltaNight*(h-14))
    elif h<6:
        minHour=maxDaily-(deltaNight*(10+h)+deltaNight)
        maxHour=maxDaily-(deltaNight*(10+h))
    print('h={},minh={},maxh={}'.format(h,round(minHour,1),round(maxHour,1)))
    return [round(minHour,1),round(maxHour,1)]
# avg_do()

def avg_level_battery(maxDailyBtr,minDailyBtr):
    # minDailyBtr=11.9
    # maxDailyBtr=13.4
    deltaUp=(maxDailyBtr-minDailyBtr)/4
    deltaDown=(maxDailyBtr-minDailyBtr)/20
    if h>8 and h<14:
        levelBtr=minDailyBtr+(deltaUp*(h-9))
    elif h>13:
        levelBtr=maxDailyBtr-(deltaDown*(h-13))
    elif h<9:
        levelBtr=maxDailyBtr-(deltaDown*(11+h))
    print('level battery: ',levelBtr)
    return levelBtr
# avg_level_battery()

def avg_temp(maxTemp,minTemp):
    # maxTemp=21.9
    # minTemp=20.1
    deltaUp=(maxTemp-minTemp)/7
    deltaDown=(maxTemp-minTemp)/17
    if h>6 and h<14:
        levelTemp=round(minTemp+(deltaUp*(h-7)),1)
    elif h>13:
        levelTemp=round(maxTemp-(deltaDown*(h-14)),1)
    elif h<7:
        levelTemp=round(maxTemp-(deltaDown*(11+h)),1)
    print('level temp: ',levelTemp)
    return levelTemp
# avg_temp()
