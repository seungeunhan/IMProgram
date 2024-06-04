from tkinter import *
import tkinter as tk
import PIL.Image
import PIL.ImageTk
from OrderUI import OrderUI
from InventoryUI import InventoryUI
from SangMi_UI import SangMi_UI
from Sales import Sales

#PIL = pip install pillow 


class MainUi:
#<기능 구현부>------------------------------------------------------------------
    def WINODW_ORDER(self):
        od = OrderUI()
        od.OrderUI_Call()

    def WINODW_SALES(self):
        sa = Sales()
        sa.Sales_Call()
    
    def WINDOW_INVENTORY(self):
        iv = InventoryUI()
        iv.ShowInventory()

    def WINDOW_SANGMI(self):
        sm = SangMi_UI()
        sm.show_SangMi()

#<GUI 구현부>-------------------------------------------------------------------
    def MainUi_Call(self):
        win = tk.Tk()

        win.title("투썸 재고 관리 시스템")  # 창 제목
        # 창 넓이, 높이 사이즈
        width = 800
        height = 600

        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        win.resizable(False,False)

        # 창 위치 계산
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        win.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #프레임
        all_Frame = Frame(win, width=800, height=550, background='#C0C0C0')          
        all_Frame.place(x=0,y=0)


        #창 아이콘 설정
        ico = tk.PhotoImage(file='image_zip/twosomelogo.png')
        win.iconphoto(False, ico)

        #캔버스와 텍스트 입력
        canvas = tk.Canvas(win, width=800, height=530, background='#474747',highlightthickness = 0)
        canvas.place(x=0, y=70)

        canvas.create_text(50,50,text="관리",fill="white",font=("맑은 고딕",23,"bold"))


        #버튼 만들기(첫째줄)
        btn_order = tk.Button(win, text="발주", justify="center",width=13, height=4,background="white",relief="solid",borderwidth="1",font=("맑은 고딕",15),
                              command=self.WINODW_ORDER)
        btn_store = tk.Button(win, text="입고", justify="center",width=13, height=4,background="white",relief="solid",borderwidth="1",font=("맑은 고딕",15))
        btn_inven = tk.Button(win, text="재고", justify="center",width=13, height=4,background="white",relief="solid",borderwidth="1",font=("맑은 고딕",15),
                            command=self.WINDOW_INVENTORY)
        btn_sanmi = tk.Button(win, text="상미", justify="center",width=13, height=4,background="white",relief="solid",borderwidth="1",font=("맑은 고딕",15),
                              command=self.WINDOW_SANGMI)
        btn_blank1 = tk.Button(win, text="", justify="center",padx=72, pady=55,background="white",relief="solid",borderwidth="1",state=tk.DISABLED)

        btn1=[btn_order,btn_store,btn_inven,btn_sanmi,btn_blank1]
        num=23
        for btn_first in btn1 :
            btn_first.place(x=num,y=197)
            num=num+150

        #버튼 만들기(둘째줄)
        btn2=["blank2", "blank3", "blank4", "blank5", "blank6"]
        num=23
        for btn_blank in btn2 :
            btn_blank = tk.Button(win, text="", justify="center",padx=72, pady=55,background="white",relief="solid",borderwidth="1",state=tk.DISABLED)
            btn_blank.place(x=num, y=324)
            num=num+150

        #버튼 만들기(셋째줄)
        btn_blank7 = tk.Button(win, text="", justify="center",padx=72, pady=55,background="white",relief="solid",borderwidth="1", state=tk.DISABLED)
        btn_sales = tk.Button(win, text="매출", justify="center",width=13, height=4,background="white",relief="solid",borderwidth="1",font=("맑은 고딕",15),
                              command=self.WINODW_SALES)
        btn_blank8 = tk.Button(win, text="", justify="center",padx=72, pady=55,background="white",relief="solid",borderwidth="1",state=tk.DISABLED)
        btn_blank9 = tk.Button(win, text="", justify="center",padx=72, pady=55,background="white",relief="solid",borderwidth="1",state=tk.DISABLED)
        btn_blank10 = tk.Button(win, text="", justify="center",padx=72, pady=55,background="white",relief="solid",borderwidth="1",state=tk.DISABLED)

        btn3=[btn_blank7,btn_sales,btn_blank8,btn_blank9,btn_blank10]
        num=23
        for btn_third in btn3 :
            btn_third.place(x=num,y=455)
            num=num+150

        win.mainloop()

#ma = MainUi()
#ma.MainUi_Call()
