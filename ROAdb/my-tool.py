from tkinter import *
from ROAdb.nihao import Detect,FN
import time
def btn_screen_short_event():
    d=Detect()
    d.background_screenshot(True)
def btn_trade_pull():
    while 1:
        f=FN()
        price = int(p.get())
        qty = int(q.get())
        f.purchase_item(lowerPrice=price,qty=qty)
        time.sleep(1)





win = Tk()

win.title('a5a5aa555oo')
win.geometry('500x300')
win.resizable(0,0)
# win.iconbitmap('image.ico')
win.attributes("-alpha",0.95)
win.attributes('-topmost',1)



btnScreenShot = Button(win, text="【開發者模式】截圖", bg='pink',command=btn_screen_short_event).grid(column=0,row=10)


# 第一行
lbTradePrice = Label(win, text="最低價格").grid(column=0,row=0)
p=StringVar()
p.set('371')
tbTradePrice = Entry(win,textvariable=p).grid(column=1,row=0)

lbQty = Label(win, text="購買數量 max:99").grid(column=2,row=0)
q=StringVar()
q.set('2')
tbQty = Entry(win,textvariable=q,width=5).grid(column=3,row=0) #state='disabled'


btnTradePull = Button(win, text="交易所搶礦石", bg='gray',command=btn_trade_pull).grid(column=4,row=0)
lbTradePriceNotice = Label(win, text="※要開啟交易所").grid(column=5,row=0)

# 第二行



#
#
#
# # name = Label(win, text="Name").place(x=30, y=50)
# # email = Label(win, text="Email").place(x=30, y=90)
# # lbStatus = Label(win, text="當前狀態").place(x=30, y=130)
# btnScreenShot = Button(win, text="當前遊戲畫面截圖", bg='pink',command=btn_screen_short_event).place(x=30, y=170)
#
# btnTrade = Button(win, text="交易所搶礦石", bg='pink',command=btn_screen_short_event).place(x=60, y=200)
#
# p=StringVar()
# p.set('125')
# tbPrice = Entry(win,textvariable=p).place(x=150, y=200)
#
# # e1 = Entry(win).place(x=80, y=50)
# # e2 = Entry(win).place(x=80, y=90)
# # e=StringVar()
# # e.set('FUCK')
# # tbStatus = Entry(win,state='disabled',textvariable=e).place(x=95, y=130)





win.mainloop()


