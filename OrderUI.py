from tkinter import *
import tkinter as tk
import tkinter.ttk
from Order_Helper import Order_Helper
from Order_Alarm import Order_Alarm
from Order_PAN import Order_PAN

class OrderUI:
    

    def OrderAlarm(self):
        od = Order_Alarm()
        od.Order_Alarm_Call()
    def Order_Check(self):
        od = Order_Helper()
        result = od.Data_Check()
        return result
    def OrderRegist(self):
        od = Order_PAN()
        od.Order_PAN_Call()
    def recall(self):
        self.treeview.delete(*self.treeview.get_children())
        self.treelist = []
        self.treelist = self.Order_Check()
        for i in range(len(self.treelist)):
            self.treeview.insert("", "end", text=i+1, values=self.treelist[i], iid=str(i))  

    # 소팅을 위한 함수입니다.
    def Sort_by_comboBox(self):
        sort_kind = self.combobox1.get()
        sort_state = self.combobox.get()
        lst = self.Order_Check()
        
        # treeview에 있던 요소들 초기화(삭제)
        self.treeview.delete(*self.treeview.get_children())


        if sort_kind == "주문일자":
            if sort_state == "오름차순":
                sorted_lst = sorted(lst, key=lambda lst:lst[1])
                #데이터 삽입
                for i in range(len(sorted_lst)):
                    self.treeview.insert("", "end", text=i+1, values=sorted_lst[i], iid=str(i))


            elif sort_state == "내림차순":
                sorted_lst = sorted(lst, key=lambda lst:lst[1], reverse=True)
                #데이터 삽입
                for i in range(len(sorted_lst)):
                    self.treeview.insert("", "end", text=i+1, values=sorted_lst[i], iid=str(i))

        elif sort_kind == "진행상태":
            if sort_state == "오름차순":
                sorted_lst = sorted(lst, key=lambda lst:lst[5])
                #데이터 삽입
                for i in range(len(sorted_lst)):
                    self.treeview.insert("", "end", text=i+1, values=sorted_lst[i], iid=str(i))


            elif sort_state == "내림차순":
                sorted_lst = sorted(lst, key=lambda lst:lst[5], reverse=True)
                #데이터 삽입
                for i in range(len(sorted_lst)):
                    self.treeview.insert("", "end", text=i+1, values=sorted_lst[i], iid=str(i))


    def OrderUI_Call(self):            
        self.win = tk.Toplevel()

        self.win.title("발주")  # 창 제목

        # 창 넓이, 높이 사이즈
        width = 1000
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

        # 투썸로고 이미지
        logo_img = PhotoImage(file="image_zip/twosomelogo1.png")
        pLabel = Label(self.win, image=logo_img, borderwidth=0, bg="#F5F5F5")
        pLabel.place(x=0, y=25)

        #발주 탭
        notebook=tkinter.ttk.Notebook(self.win, width=960, height=550)
        order=tkinter.Frame(self.win,bg="white")
        label = Label(self.win, text= "발   주", width=7, height=1,bg="#474747", fg="white", font=("맑은 고딕", 11))
        label_line = Label(self.win, text= "", width=894, height=1,bg="#808080", font=("맑은 고딕", 1))
        label.place(x=19, y=110)
        label_line.place(x=50, y=192)
        notebook.place(x=19, y=135)


        #새로고침 버튼
        change_img_btn = PhotoImage(file="image_zip/새로고침버튼.png")
        btn_ch = tk.Button(self.win,image=change_img_btn, padx=72, pady=50,relief="groove",borderwidth="0",command=self.recall)
        btn_ch.place(x=684,y=100)


        #알림버튼
        Alarm_img_btn = PhotoImage(file="image_zip/알림버튼.png")
        btn_od = tk.Button(self.win,image=Alarm_img_btn, padx=72, pady=50,relief="groove",borderwidth="0",command=self.OrderAlarm)
        btn_od.place(x=765,y=100)


        #등록버튼
        regist_img_btn = PhotoImage(file="image_zip/등록버튼.png")
        btn_rg = tk.Button(self.win,image=regist_img_btn, padx=72, pady=50,relief="groove",borderwidth="0",command=self.OrderRegist)
        btn_rg.place(x=820,y=100)

        #수정버튼
        update_img_btn = PhotoImage(file="image_zip/수정버튼.png")
        btn_up = tk.Button(self.win,image=update_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_up.place(x=875,y=100)

        #삭제버튼
        delete_img_btn = PhotoImage(file="image_zip/삭제버튼.png")
        btn_del = tk.Button(self.win,image=delete_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_del.place(x=930,y=100)

        #검색버튼
        search_img_btn = PhotoImage(file="image_zip/검색.png")
        btn_search = tk.Button(self.win,image=search_img_btn, padx=72, pady=50,relief="flat",borderwidth="0", bg="white", command=self.Sort_by_comboBox)
        btn_search.place(x=945,y=155)

        #콤보박스
        self.sort_state1=["주문일자", "진행상태"]        # 콤보 박스에 나타낼 항목 리스트
        self.combobox1 = tkinter.ttk.Combobox(self.win)       # root라는 창에 콤보박스 생성
        self.combobox1.config(width=9,height=5, values=self.sort_state1, state="readonly", font=("맑은 고딕",10)) 
        self.combobox1.set(self.sort_state1[0])                   # 맨 처음 나타낼 값 설정
        self.combobox1.place(x=620, y=152)

        self.sort_state=["오름차순", "내림차순"]        # 콤보 박스에 나타낼 항목 리스트
        self.combobox = tkinter.ttk.Combobox(self.win)       # root라는 창에 콤보박스 생성
        self.combobox.config(width=9, values=self.sort_state, state="readonly",font=("맑은 고딕",10)) 
        self.combobox.set(self.sort_state[0])                   # 맨 처음 나타낼 값 설정
        self.combobox.place(x=710, y=152) 

        #텍스트 박스(entry)(검색)
        text_search= tk.Entry(self.win, width=18, font=("맑은 고딕",10), borderwidth=2, foreground="#333333")
        text_search.place(x= 805, y= 152)

        # 트리뷰(표)------------------------------------------------------------
        column=["품목명", "날짜", "단가", "갯수","합계","진행상태"]   #컬럼명
        self.treeview=tkinter.ttk.Treeview(self.win, columns=column)  #트리뷰 생성

        self.treeview.place(x=50, y=200, height=470, width=900)  #표 위치, 사이즈

        #세로 스크롤바 생성
        scroll_y = Scrollbar(self.win, orient=VERTICAL)
        scroll_y.place(x=927, y=201, width=22, height=468)
        self.treeview.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=self.treeview.yview)

        #컬럼 컬럼명, 넓이, 정렬
        self.treeview.column("#0", width=10,anchor="center")
        self.treeview.heading("#0", text="No",anchor="center")
        for col_lis in column :
            if col_lis=="발주날짜" or col_lis=="합계액" or col_lis=="진행상태":
                self.treeview.column(col_lis,width=300,anchor="center")
                self.treeview.heading(col_lis, text=col_lis, anchor="center")
            self.treeview.column(col_lis, width=80, anchor="center")
            self.treeview.heading(col_lis, text=col_lis, anchor="center")
        treelist = self.Order_Check()
        data_list =[]
        for i in treelist:

            data_list.append(list(i))
                    


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

                
                """
        #데이터 삽입
        for i in range(len(treelist)):
            self.treeview.insert("", "end", text=i+1, values=treelist[i], iid=str(i))
        self.win.mainloop()
        
#od = OrderUI()
#od.OrderUI_Call()