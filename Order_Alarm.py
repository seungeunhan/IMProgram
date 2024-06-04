from tkinter import *
import tkinter as tk
import tkinter.ttk
from datetime import date
from Order_Helper import Order_Helper
class Order_Alarm:
    def AlarmRegist(self):
        od = Order_Helper

        # treeview에 있던 요소들 초기화(삭제)
        self.treeview.delete(*self.treeview.get_children())
        
        # 앞으로 보여줄 리스트 데이터(선택된것 삭제된 리스트)
        newTreeList = [i for i in self.treelist if i != tuple(self.values)]
        
        # 트리뷰에 수정된 데이터 삽입
        for i in range(len(newTreeList)):
            self.treeview.insert("", "end", text=i+1, values=newTreeList[i], iid=str(i))
        od.Order_format_n_reg(self, self.values)


    def click_item(self,event):
        item_id = self.treeview.focus()
        item_data = self.treeview.item(item_id)
        self.values = item_data['values']
         
        print('선택된 아이템 :', self.values)   
    def Alarm_Check(self):
        od = Order_Helper()
        result = od.Inventory_Check()
        print(result)
        return result
    def Order_Alarm_Call(self):
        self.win = tk.Toplevel()
        self.win.title("발주제안알림")  # 창 제목

        # 창 넓이, 높이 사이즈
        width = 600
        height = 700

        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        self.win.resizable(False,False)

        # 창 위치 계산
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.win.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #창 백그라운드 색상
        self.win.configure(bg='#F5F5F5')

        #창 아이콘 설정 
        ico = tk.PhotoImage(file='image_zip/twosomelogo.png')
        self.win.iconphoto(False, ico)

        #발주제안알림 라벨
        Alarm = Label(self.win, text= "발주제안알림", width=10,height=1,bg="#F5F5F5", font=("맑은 고딕", 13, "bold"))    #알림일자 출력
        Alarm.place(x= 20, y= 45)

        # 알람정보
        canvas = tk.Canvas(self.win, width=532, height=132, background='#F5F5F5',highlightthickness = 0)
        canvas.place(x=35, y=85)
        canvas.create_rectangle(3, 0, 527, 130, fill='white', outline='#A0A0A0', width=1)         #사각형 테두리

        canvas.create_rectangle(3, 0, 131, 44, fill='#E0E0E0', outline='#A0A0A0', width=1)        #알림일자 도형
        canvas.create_text(68,22,text="알람일자",fill="black",font=("맑은 고딕",11))                #알림일자 글자 삽입

        today = date.today()
        formatted_date = today.strftime('%Y년 %m월 %d일')

        Alarmdate = Label(self.win, text= formatted_date, width=50,height=2,bg="white", font=("맑은 고딕", 10),borderwidth=1)    #알람일자 출력
        Alarmdate.place(x= 187, y= 88)

        canvas.create_rectangle(3, 44, 131, 86, fill='#E0E0E0', outline='#A0A0A0', width=1)       #지점코드 도형
        canvas.create_text(68,65,text="지점코드",fill="black",font=("맑은 고딕",11))                #지점코드 글자 삽입

        canvas.create_rectangle(131, 44, 261, 86, fill='white', outline='#A0A0A0', width=1)       #지점코드 도형
        canvas.create_text(200,65,text="101",fill="black",font=("맑은 고딕",11))                   #지점코드  삽입

        canvas.create_rectangle(261, 44, 380, 86, fill='#E0E0E0', outline='#A0A0A0', width=1)      #지점명 도형
        canvas.create_text(320,65,text="지 점 명",fill="black",font=("맑은 고딕",11))                 #지점명 글자 삽입

        canvas.create_rectangle(375, 44, 527, 86, fill='white', outline='#A0A0A0', width=1)       #지점명 도형
        canvas.create_text(451,65,text="투썸플레이스 OO점",fill="black",font=("맑은 고딕",11))                   #지점명 삽입

        canvas.create_rectangle(3, 86, 131, 130, fill='#E0E0E0', outline='#A0A0A0', width=1)      #합계액 도형
        canvas.create_text(68,108,text="합 계 액",fill="black",font=("맑은 고딕",11))              #합계액 글자 삽입

        Total_sum = Label(self.win, text= "", width=43,height=2,bg="white", font=("맑은 고딕", 10),borderwidth=1)   #합계액 출력
        Total_sum.place(x= 257, y= 174)


        #등록버튼
        regist_img_btn = PhotoImage(file="image_zip/등록버튼.png")
        btn_rg = tk.Button(self.win,image=regist_img_btn, padx=72, pady=50,relief="groove",borderwidth="0",command=self.AlarmRegist)
        btn_rg.place(x=475,y=255)

        #삭제버튼
        delete_img_btn = PhotoImage(file="image_zip/삭제버튼.png")
        btn_del = tk.Button(self.win,image=delete_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_del.place(x=530,y=255)

        #표 상단 막대
        label_line = Label(self.win, text= "", width=555, height=1,bg="#808080", font=("맑은 고딕", 1))
        label_line.place(x=20, y=292)

        #트리뷰(매출조회)
        column=["제품명", "현재 재고 갯수", "단가"]   #컬럼명
        self.treeview=tkinter.ttk.Treeview(self.win, columns=column)  #트리뷰 생성

        self.treeview.place(x=20, y=300, height=370, width=560)  #표 위치, 사이즈


        #세로 스크롤바 생성
        scroll_y = Scrollbar(self.win, orient=VERTICAL)
        scroll_y.place(x=557, y=301, width=22, height=368)
        self.treeview.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=self.treeview.yview)

        #컬럼 컬럼명, 넓이, 정렬
        self.treeview.column("#0", width=10,anchor="center")
        self.treeview.heading("#0", text="No",anchor="center")
        for col_lis in column :
            if col_lis=="매출일자" or col_lis=="합계액" or col_lis=="진행상태":
                self.treeview.column(col_lis,width=300,anchor="center")
                self.treeview.heading(col_lis, text=col_lis, anchor="center")
            self.treeview.column(col_lis, width=80, anchor="center")
            self.treeview.heading(col_lis, text=col_lis, anchor="center")

        #표 내용(test용)
        self.treelist=self.Alarm_Check()

        #데이터 삽입
        for i in range(len( self.treelist)):
            self.treeview.insert("", "end", text=i+1, values= self.treelist[i], iid=str(i))

        self.treeview.bind('<ButtonRelease-1>', self.click_item)
        self.win.mainloop()

#od1 = Order_Alarm()
#od1.Order_Alarm_Call()


