import os
import time
from datetime import datetime
from ROAdb.nihao import FN,Detect

def get_odd_minutes():
    now = datetime.now()
    print("當前時間: ",now.strftime("%H:%M:%S"))
    timeStr = now.strftime("%H")
    if int(timeStr) %2 !=0:
        return int(now.strftime("%M"))
    else:
        return 0


def stop_fight():
    d = Detect()
    d.click_event(822, 550)  # 停止戰鬥


def go_to_weeds():
    print('拔草時間---')
    #TODO 判斷是否正在拔草 <---> 判斷是否戰鬥中
    fn = FN()
    if fn.check_auto_attack2()=="戰鬥中":
        stop_fight()
        time.sleep(0.9)
        # 檢查生活有沒有開啟，點生活採集...
        pass
    # elif fn.check_is_on_flowering():
        # 拔草

    pass

if __name__ == '__main__':
    flag = 0
    while flag==0:
        currentMinute= get_odd_minutes()
        if currentMinute >= 55: #超過55分
            flag=1
            go_to_weeds()
        else :
            time.sleep(1)
        # time.sleep(1)

        # 判斷當前時間
