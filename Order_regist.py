#### 이건 안쓰는 파일 ####


from tkinter import *
import tkinter as tk
import tkinter.ttk
import gc
from datetime import date
from Order_Helper import Order_Helper


class Order_regist:
    def OrderRegist1(self):
        FindWord = self.text_pd.get()
        if(len(FindWord) == 0):
            self.win.destroy()
            from Order_PAN import Order_PAN
            od = Order_PAN()
            od.Order_PAN_Call()
            gc.collect()


    def OrderAccept(self):
        print('완료')

    def Order_Search1(self):
        od = Order_Helper()
        result = od.Data_Check()
        for i in result:
            self.Pd_Data.append(list(i))
        

        for i in range(len(self.Pd_Data)):
            self.treeview.insert("", "end", text=i+1, values=self.Pd_Data[i], iid=str(i))        
    def Order_regist_Call(self):
        self.win = tk.Toplevel()
        self.win.title("발주등록")  # 창 제목

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
        Alarm_lb = Label(self.win, text= "발주등록", width=10,height=1,bg="#F5F5F5", font=("맑은 고딕", 13, "bold"))    #발주제안알림 글자 출력
        Alarm_lb.place(x= 5, y= 45)


        # 알람정보
        canvas = tk.Canvas(self.win, width=532, height=132, background='#F5F5F5',highlightthickness = 0)
        canvas.place(x=35, y=85)
        canvas.create_rectangle(3, 0, 527, 130, fill='white', outline='#A0A0A0', width=1)         #사각형 테두리

        canvas.create_rectangle(3, 0, 131, 44, fill='#E0E0E0', outline='#A0A0A0', width=1)        #주문번호 도형
        canvas.create_text(68,22,text="주문번호",fill="black",font=("맑은 고딕",11))                #주문번호 글자 삽입

        OrderNum = Label(self.win, text="", width=14,height=2,bg="white", font=("맑은 고딕", 11),relief="groove",borderwidth=1)    #주문번호 출력
        OrderNum.place(x= 166, y= 85)
        today = date.today()
        formatted_date = today.strftime('%Y년 %m월 %d일')
        canvas.create_rectangle(261, 0, 375, 86, fill='#E0E0E0', outline='#A0A0A0', width=1)      #주문일자 도형
        canvas.create_text(320,22,text="주문일자",fill="black",font=("맑은 고딕",11))

        OrderDate = Label(self.win, text= formatted_date, width=16,height=2,bg="white", font=("맑은 고딕", 10),borderwidth=1)    #주문일자 출력
        OrderDate.place(x= 428, y=88)

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


        #품목명 라벨
        pd_name = Label(self.win, text= "품목명", width=10,height=1,bg="#F5F5F5", font=("맑은 고딕", 10))    #품목명 글자 출력
        pd_name.place(x= 20, y= 255)

        #텍스트 박스(entry)(품목명)
        self.text_pd = tk.Entry(self.win, width=14, font=("맑은 고딕",13), borderwidth=1, foreground="#333333")
        self.text_pd.place(x= 90, y= 255)

        #검색버튼(돋보기 이미지)
        search_img_btn = PhotoImage(file="image_zip/검색.png")
        btn_search = tk.Button(self.win,image=search_img_btn, padx=72, pady=50,relief="flat",borderwidth="0", bg="white",command=self.OrderRegist1)
        btn_search.place(x=228,y=260)

        #완료버튼
        regist_img_btn = PhotoImage(file="image_zip/완료버튼.png")
        btn_rg = tk.Button(self.win,image=regist_img_btn, padx=72, pady=50,relief="groove",borderwidth="0",command=self.OrderAccept)
        btn_rg.place(x=475,y=255)

        #삭제버튼
        delete_img_btn = PhotoImage(file="image_zip/삭제버튼.png")
        btn_del = tk.Button(self.win,image=delete_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_del.place(x=530,y=255)

        #표 상단 막대
        label_line = Label(self.win, text= "", width=555, height=1,bg="#808080", font=("맑은 고딕", 1))
        label_line.place(x=20, y=292)

        #트리뷰(매출조회)
        column=["체크", "매출일자", "합계액", "진행상태"]   #컬럼명
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
            if col_lis=="제품명" or col_lis=="합계액" or col_lis=="진행상태":
                self.treeview.column(col_lis,width=300,anchor="center")
                self.treeview.heading(col_lis, text=col_lis, anchor="center")
            self.treeview.column(col_lis, width=80, anchor="center")
            self.treeview.heading(col_lis, text=col_lis, anchor="center")
        self.treelist = []
        self.Pd_Data = []
        self.Order_Search1()

        #표 내용(test용)
        """
        treelist=[("공백", "2023-03-01", "135,500","진행완료"), ("공백", "2023-03-05", "500,000","진행완료"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-01", "135,500","진행완료"), ("공백", "2023-03-05", "500,000","진행완료"),
                ("공백", "2023-03-01", "135,500","진행완료"), ("공백", "2023-03-05", "500,000","진행완료"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-06", "235,000","진행대기"), ("공백", "2023-03-08", "606,000","진행대기"),
                ("공백", "2023-03-01", "135,500","진행완료"), ("공백", "2023-03-05", "500,000","진행완료"),]

        #데이터 삽입
        for i in range(len(treelist)):
            treeview.insert("", "end", text=i+1, values=treelist[i], iid=str(i))
        """
        self.win.mainloop()

#og = Order_regist()
#og.Order_regist_Call()