import random
import subprocess
import threading
import time

import numpy
import plot as plot
import win32con
import win32gui
import win32ui
import cv2
from PIL import Image
from PIL import ImageGrab

import imagehash
import pytesseract
import numpy as np
import os
import matplotlib.pyplot as plt
import ocrapi
from threading import Thread
from datetime import datetime



class Detect:
    def __init__(self):
        # self.ldName=ldName
        self.hwnd = win32gui.FindWindow(None, "RO")
        self.width=1280
        self.height=760
        self.device_name="127.0.0.1:5555"
        self.ADB_Path = r"C:\LDPlayer\LDPlayer3.0\adb.exe"
        self.tessPath ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        self.tempPicture = None
    def keep_screen_hot(self):
        th = Thread(target=self.keep_screen_hot_fn)
        th.start()
    def keep_screen_hot_fn(self):
        while 1:
            self.background_screenshot(True)
            time.sleep(1)


    def background_screenshot(self,isDebug):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.width, self.height), dcObj, (0, 0), win32con.SRCCOPY)
        # dataBitMap.SaveBitmapFile(cDC, fileName)
        ##PIL保存
        ###获取位图信息
        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)
        im_PIL = Image.frombuffer('RGB',
                                  (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
                                  bmpstr, 'raw', 'BGRX', 0, 1)
        im_PIL = im_PIL.crop((0,36,self.width,self.height))
        if isDebug:
            print('更新截圖 screenshot.png')
            im_PIL.save('screenshot.png')

        ###生成图像
        self.tempPicture = im_PIL

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return im_PIL

    def adb_call(self,detail_list):
        command = [self.ADB_Path,'-s',self.device_name]
        for order in detail_list:
            command.append(order)
        print(command)
        subprocess.Popen(command)
    def click_event(self,x,y):
        x = str(x)
        y = str(y)
        self.adb_call(['shell','input','tap',x,y])
    def Image_CMP(self,sample_img_name,source_img):
        time.sleep(1)
        sample_img_name = os.path.join(os.getcwd(),sample_img_name)
        source_img = os.path.join(os.getcwd(),source_img)

        Sample_img = Image.open(sample_img_name)
        Sample_hash = imagehash.phash(Sample_img)
        Source_img = Image.open(source_img)
        source_hash = imagehash.phash(Source_img)

        Point = Sample_hash - source_hash

        return Point


    def Cutting_Image(self,src,p1,p2,p3,p4,target):
        im = cv2.imread(src)
        point1 = (p1,p2)
        point2 = (p3,p4)
        crop = im[point1[1]:point2[1],point1[0]:point2[0]]

        taget = os.path.join(os.getcwd(),target)
        cv2.imwrite(taget,crop)

    def system_btn(self,name):
        btn_map = {}
        btn_map['1'] = [532, 290]
        btn_map['2'] = [880, 290]
        btn_map['3'] = [950, 290]
        btn_map['4'] = [810, 360]
        btn_map['5'] = [880, 360]
        btn_map['6'] = [950, 360]
        btn_map['7'] = [810, 435]
        btn_map['8'] = [880, 435]
        btn_map['9'] = [950, 435]
        btn_map['O'] = [1025, 435]
        btn_map['X'] = [1025, 290]
        btn_map['園藝'] = [795, 290]

        if name not in btn_map:
            print("無此按鍵名稱：{}".format(name))
            return 0

        click_loc = btn_map[name]
        self.click_event(click_loc[0], click_loc[1])



    def compare_diff_price(self,lowPrice,qty):




        time.sleep(0.5)
        self.click_event(532, 230)
        time.sleep(1)
        d = self.background_screenshot(False)
        time.sleep(0.1)

        d = d.crop((883,216,938,244))

        # d.save('temp_price.png')
        # 圖片灰階
        img = numpy.array(d)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # t, binary = cv2.threshold(gray, 0, 255,
        #                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        mask_inv = cv2.bitwise_not(gray)  # 取反，把黑底白字变白底黑字

        plt.imshow(mask_inv)
        plt.show()
        # cv2.imshow('s',mask_inv)
        # cv2.waitKey()

        text = pytesseract.image_to_string(mask_inv, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        result = text
        print(result)

        try:
            result = int(text)
            if lowPrice > result > 100:
                self.BuyingItem()
        except:
            result = 0


        self.click_event(618,103)

        return  result

    def BuyingItem(self):
        self.click_event(532,383)
        time.sleep(0.5)
        # self.click_event(533,290)
        self.click_event(673,436)
        time.sleep(0.5)
        self.click_event(673,436)
        time.sleep(0.5)
        self.click_event(748,436)
        time.sleep(0.5)
        self.click_event(416,602)
        time.sleep(7)




class FN:
    def __init__(self):
        self.src_path=os.path.join(os.getcwd(),'images/temp')
        self.sample_path=os.path.join(os.getcwd(),'images/sample')
        self.status=''

    def check_auto_attack(self):
        d = Detect()
        img = d.background_screenshot(True)
        img = img.crop((806,520,837,559))
        src= os.path.join(self.src_path,'on-attack.png')
        img.save(src)

        is_diff_val = d.Image_CMP(os.path.join(self.sample_path,'on-attack.png'),src)
        print(is_diff_val)

        if is_diff_val==0:
            self.status='戰鬥中'
        else:
            d.click_event(826,548)
            time.sleep(1)
            d.click_event(1129,443)
            time.sleep(1)
            d.click_event(822,432)
            time.sleep(1)
        return self.status

    def check_auto_attack2(self):
        d = Detect()
        img = d.background_screenshot(True)
        img = img.crop((806,520,837,559))
        src= os.path.join(self.src_path,'on-attack.png')
        img.save(src)

        is_diff_val = d.Image_CMP(os.path.join(self.sample_path,'on-attack.png'),src)
        print(is_diff_val)

        if is_diff_val==0:
            return "戰鬥中"
        else:
            return "拔草中"

    def find_monster(self,monster_name):
        d = Detect()
        img = d.background_screenshot(False)
        img = img.crop((956,20,996,58))
        src= os.path.join(self.src_path,'is-opening.png')
        img.save(src)
        is_diff_val = d.Image_CMP(os.path.join(self.sample_path,'is-opening.png'),src)
        if is_diff_val ==0 :
            d.click_event(970,42)
            time.sleep(1.5)
            d.click_event(1164,238)
            time.sleep(1.5)
            d.click_event(793, 76)
            time.sleep(1.5) # send key error

    def pull_up_weeds(self):
        d= Detect()
        d.background_screenshot(True)

    def purchase_item(self,lowerPrice,qty):
        d = Detect()
        d.click_event(170,114)
        time.sleep(0.5)
        price = d.compare_diff_price(lowPrice=lowerPrice,qty=qty)
        print(price)
        time.sleep(5)

    def fishing(self):
        d = Detect()
        img = d.background_screenshot(False)
        img = img.crop((1065,421,1137,589))
        src= os.path.join(self.src_path,'is-pulling.png')
        img.save(src)
    def check_life_isExpanding(self):
        return True
    def stop_attack_and_go_to_weeds(self):
        d = Detect()
        img = d.background_screenshot(False)
        img = img.crop((806, 520, 837, 559))
        src = os.path.join(self.src_path, 'on-attack.png')
        img.save(src)

        is_diff_val = d.Image_CMP(
            os.path.join(self.sample_path, 'on-attack.png'), src)

        if is_diff_val == 0:
            self.status = '戰鬥中'
            d.click_event(826,548)
            time.sleep(1)
            if self.check_life_isExpanding():
                d.click_event(1114,499) #生活
                time.sleep(1)
                d.click_event(409,638) #園藝
                time.sleep(1)
                d.click_event(338,662) #枯荊棘
                time.sleep(1)
                d.click_event(775,498) #採集點2
                
    def auto_kanban(self):
        d = Detect()
        #TODO // 判斷展開
        # d.click_event(894,43) # 嘉年華
        # time.sleep(0.5)
        # d.click_event(642,468) # 委託版
        # time.sleep(0.5)
        # d.click_event(636,590) # 立即前往
        # time.sleep(0.5)


        x = 230
        # for i in range(0,5):
        #     d.click_event(x+i*250, 230)  # 第一個
        #     time.sleep(1.5)
        #     d.click_event(657, 571)  # 接受
        #     time.sleep(1.5)

        for i in range(0,5):
            d.click_event(x+i*235, 450)  # 第一個
            time.sleep(1.5)
            d.click_event(657, 571)  # 接受
            time.sleep(1.5)


        pass





def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
def get_current_hour_number():
    now = datetime.now()
    return int(now.strftime("%H"))

if __name__ == '__main__':
    f = FN()
    f.auto_kanban()
    # while 1:
    #     current_time = get_current_time()
    #     currentHourNumber = get_current_hour_number()
    #     f = FN()
    #     if currentHourNumber % 2 == 0:
    #         print('偶數時間---拔草')
    #         f.stop_attack_and_go_to_weeds()
    #         # d = Detect()
    #         # img = d.background_screenshot(True)


    #
    #
    # d = Detect()
    # d.keep_screen_hot()
    # while d.tempPicture is None:
    #     print("等待…")
    #     time.sleep(0.1)
    #
    # print(d.tempPicture)

