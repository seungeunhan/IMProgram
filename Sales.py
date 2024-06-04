from tkinter import *
import tkinter as tk
import tkinter.ttk
from Sales_Helper import Sales_Helper

class Sales:


    def Check_Sales(self):
        helper = Sales_Helper
        result = helper.Check_Sales()
        print('boundery class Sales come data')
        return result

    # 소팅을 위한 함수입니다.
    def Sort_by_comboBox(self):
        sort_state = self.combobox.get()
        lst = self.Check_Sales()
        
        # treeview에 있던 요소들 초기화(삭제)
        self.treeview.delete(*self.treeview.get_children())

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

    def Sales_Call(self):
        win = tk.Toplevel()

        win.title("매출")

        width = 1000
        height = 700

        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        win.resizable(False,False)

        # 창 위치 계산
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        win.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #창 백그라운드 색상
        win.configure(bg='#F5F5F5')

        #창 아이콘 설정
        ico = tk.PhotoImage(file='image_zip/twosomelogo.png')
        win.iconphoto(False, ico)

        # 투썸로고 이미지
        logo_img = PhotoImage(file="image_zip/twosomelogo1.png")
        pLabel = Label(win, image=logo_img, borderwidth=0, bg="#F5F5F5")
        pLabel.place(x=0, y=25)


        #매출조회와 일매출정보 탭
        notebook_sales_list=tkinter.ttk.Notebook(win, width=670, height=550)
        order=tkinter.Frame(win,bg="white")
        label_sales_list = Label(win, text= "매출조회", width=8, height=1,bg="#474747", fg="white", font=("맑은 고딕", 11))
        label_sales_list.place(x=19, y=110)
        notebook_sales_list.place(x=19, y=135)

        notebook_sales_info=tkinter.ttk.Notebook(win, width=280, height=550)
        order=tkinter.Frame(win,bg="white")
        label_sales_info = Label(win, text= "일매출정보", width=10, height=1,bg="#474747", fg="white", font=("맑은 고딕", 11))
        label_sales_info.place(x=700, y=110)
        notebook_sales_info.place(x=700, y=135)

        label_line = Label(win, text= "", width=644, height=1,bg="#808080", font=("맑은 고딕", 1))
        label_line.place(x=30, y=192)


        # 일 매출정보(글자)
        canvas = tk.Canvas(win, width=265, height=211, background='white',highlightthickness = 0)
        canvas.create_rectangle(0, 0, 264, 210, fill='white', outline='#808080', width=1)
        canvas.create_line(15, 135, 245, 135, fill='#808080', width=1)

        canvas.place(x=708, y=155)
        
        label_total_count = Label(win, text= "총 수 량", width=7, height=1,bg="white", font=("맑은 고딕", 13, "bold"))
        label_coffee = Label(win, text= "커피", width=3, height=1,bg="white", font=("맑은 고딕", 11))
        label_noncoffee = Label(win, text= "음료", width=3, height=1,bg="white", font=("맑은 고딕", 11))
        label_total_sales = Label(win, text= "총매출액", width=7, height=1,bg="white", font=("맑은 고딕", 13, "bold"))
        label_total_sales.place(x=720, y=305)
        label_noncoffee.place(x=754, y=245)
        label_coffee.place(x=754, y=215)
        label_total_count.place(x=720, y=180)

        #일매출 정보 텍스트 박스
        text_total_count= Label(win, text= "", width=14,height=1,bg="white", font=("맑은 고딕", 11),relief="groove",borderwidth=1)
        text_total_count.place(x= 820, y= 185)

        text_coffee= Label(win, text= "", width=14,height=1,bg="white", font=("맑은 고딕", 11),relief="groove",borderwidth=1)
        text_coffee.place(x= 820, y= 215)

        text_noncoffee= Label(win, text= "", width=14,height=1,bg="white", font=("맑은 고딕", 11),relief="groove",borderwidth=1)
        text_noncoffee.place(x= 820, y= 245)

        text_total_sales= Label(win, text= "", width=14,height=1,bg="white", font=("맑은 고딕", 11),relief="groove",borderwidth=1)
        text_total_sales.place(x= 820, y= 310)

        # 계산기 이미지
        cal_img = PhotoImage(file="image_zip/계산기.png")
        pLabel = Label(win, image=cal_img, borderwidth=0, bg="#F5F5F5")
        pLabel.place(x=708, y=380)

        #수정버튼
        update_img_btn = PhotoImage(file="image_zip/수정버튼.png")
        btn_up = tk.Button(win,image=update_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_up.place(x=585,y=100)

        #삭제버튼
        delete_img_btn = PhotoImage(file="image_zip/삭제버튼.png")
        btn_del = tk.Button(win,image=delete_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_del.place(x=640,y=100)

        #검색버튼
        search_img_btn = PhotoImage(file="image_zip/검색.png")
        btn_search = tk.Button(win,image=search_img_btn, padx=72, pady=50,relief="flat",borderwidth="0", bg="white", command=self.Sort_by_comboBox)
        btn_search.place(x=660,y=155)

        #콤보박스
        sort_state=["매출일자"]        # 콤보 박스에 나타낼 항목 리스트
        combobox = tkinter.ttk.Combobox(win)       # root라는 창에 콤보박스 생성
        combobox.config(width=9,height=5, values=sort_state, state="readonly", font=("맑은 고딕",10)) 
        combobox.set(sort_state[0])                   # 맨 처음 나타낼 값 설정
        combobox.place(x=335, y=152)

        sort_state=["오름차순", "내림차순"]        # 콤보 박스에 나타낼 항목 리스트
        self.combobox = tkinter.ttk.Combobox(win)       # root라는 창에 콤보박스 생성
        self.combobox.config(width=9, values=sort_state, state="readonly",font=("맑은 고딕",10)) 
        self.combobox.set(sort_state[0])                   # 맨 처음 나타낼 값 설정
        self.combobox.place(x=425, y=152) 

        #텍스트 박스(entry)(검색)
        text_search= tk.Entry(win, width=18, font=("맑은 고딕",10), borderwidth=2, foreground="#333333")
        text_search.place(x= 520, y= 152)

        #트리뷰(매출조회)
        column=["체크", "매출일자", "합계액", "진행상태","합계금액"]   #컬럼명
        self.treeview=tkinter.ttk.Treeview(win, columns=column)  #트리뷰 생성

        self.treeview.place(x=30, y=200, height=470, width=650)  #표 위치, 사이즈


        #세로 스크롤바 생성
        scroll_y = Scrollbar(win, orient=VERTICAL)
        scroll_y.place(x=657, y=201, width=22, height=468)
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
        
        treelist = self.Check_Sales() 
        #print(treelist)
        #표 내용(test용)
        """treelist=[("공백", "2023-03-01", "135,500","진행완료"), ("공백", "2023-03-05", "500,000","진행완료"),
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

        
        win.mainloop()


#sa = Sales()
#sa.Sales_Call()