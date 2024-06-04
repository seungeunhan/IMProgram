from tkinter import *
import tkinter as tk
import tkinter.ttk
import gc
from datetime import date
from ORDER_LIST import ORDER_LIST
from Order_Helper import Order_Helper

class Order_PAN:

    def Product_Check(self):
        od = ORDER_LIST()
        self.result = od.get_Product_data()
    def click_item(self,event):
        item_id = self.treeview.focus()
        item_data = self.treeview.item(item_id)
        values = item_data['values']
        self.text_df.config(state="normal")
        self.text_cost.config(state="normal")
        self.text_df.delete(0,tk.END)
        self.text_cost.delete(0,tk.END)
        self.text_df.insert(0,values[0])
        self.text_cost.insert(0,values[1])
        self.text_df.config(state="disabled")
        self.text_cost.config(state="disabled")
    def Accept_Order(self):
        product_name = self.text_df.get()
        product_cost = self.text_cost.get()
        product_count = self.text_count.get()
         
        if product_count.isdecimal():
            product_count = int(product_count)
            if(product_count == 0 or product_count < 0):
                print('잘못된 값을 설정하였습니다.')
            else:
                product_data = [[product_name,product_cost,product_count]]
                od = Order_Helper()
                od.Order_Appand(product_data)
                self.win.destroy()
                gc.collect()


    def Order_PAN_Call(self):
        self.win = tk.Toplevel()
        self.win.title("발주등록")  # 창 제목
        # 창 넓이, 높이 사이즈
        width = 400
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

        notebook=tkinter.ttk.Notebook(self.win, width=400, height=470)
        notebook.pack()

        tab1=tkinter.Frame(self.win)
        notebook.add(tab1, text="전체")

        #데이터 입력---------------------

        #품목명 라벨
        pd_name_df = Label(self.win, text= "품목명", width=8,height=1,bg="#F5F5F5", font=("맑은 고딕", 10),state="disabled")    #품목명 글자 출력
        pd_name_df.place(x= 80, y= 520)

        #텍스트 박스(entry)(품목명)
        self.text_df = tk.Entry(self.win, width=20, font=("맑은 고딕",11), borderwidth=1, foreground="#333333")
        self.text_df.place(x= 140, y= 520)

        #단가 라벨
        pd_price = Label(self.win, text= "단  가", width=8,height=1,bg="#F5F5F5", font=("맑은 고딕", 10),state="disabled")    #품목명 글자 출력
        pd_price.place(x= 80, y= 560)

        #텍스트 박스(entry)(단가)
        self.text_cost = tk.Entry(self.win, width=20, font=("맑은 고딕",11), borderwidth=1, foreground="#333333")
        self.text_cost.place(x= 140, y= 560)

        #개수 라벨
        pd_price = Label(self.win, text= "개  수", width=8,height=1,bg="#F5F5F5", font=("맑은 고딕", 10))    #품목명 글자 출력
        pd_price.place(x= 80, y= 600)

        #텍스트 박스(entry)(개수)
        self.text_count = tk.Entry(self.win, width=20, font=("맑은 고딕",11), borderwidth=1, foreground="#333333")
        self.text_count.place(x= 140, y= 600)

        #완료버튼
        regist_img_btn = PhotoImage(file="image_zip/완료버튼.png")
        btn_rg = tk.Button(self.win,image=regist_img_btn, padx=72, pady=50,relief="groove",borderwidth="0",command=self.Accept_Order)
        btn_rg.place(x=145,y=650)

        #취소버튼
        cancel_img_btn = PhotoImage(file="image_zip/취소버튼.png")
        btn_cc = tk.Button(self.win,image=cancel_img_btn, padx=72, pady=50,relief="groove",borderwidth="0")
        btn_cc.place(x=205,y=650)



        #품목명 라벨
        pd_name1 = Label(self.win, text= "품목명", width=8,height=1,bg="#F5F5F5", font=("맑은 고딕", 10))    #품목명 글자 출력
        pd_name1.place(x= 4, y= 40)

        #텍스트 박스(entry)(품목명)
        text_pd1 = tk.Entry(self.win, width=13, font=("맑은 고딕",12), borderwidth=1, foreground="#333333")
        text_pd1.place(x= 60, y= 40)

        #검색버튼(돋보기 이미지)
        search_img_btn1 = PhotoImage(file="image_zip/검색.png")
        btn_search1 = tk.Button(self.win,image=search_img_btn1,  padx=72, pady=50,relief="flat",borderwidth="0", bg="#F5F5F5")
        btn_search1.place(x=190,y=42)


        
        #콤보박스
        sort_state=["커피류", "음료류"]        # 콤보 박스에 나타낼 항목 리스트
        combobox = tkinter.ttk.Combobox(self.win)       # root라는 창에 콤보박스 생성
        combobox.config(width=9,height=5, values=sort_state, state="readonly", font=("맑은 고딕",10)) 
        combobox.set(sort_state[0])                   # 맨 처음 나타낼 값 설정
        combobox.place(x=304, y=83)

        #트리뷰(매출조회)
        column=["제품명", "단가"]   #컬럼명
        self.treeview=tkinter.ttk.Treeview(self.win, columns=column)  #트리뷰 생성
        self.treeview.place(x=10, y=125, height=360, width=380)  #표 위치, 사이즈

        #표 상단 막대
        label_line = Label(self.win, text= "", width=374, height=1,bg="#808080", font=("맑은 고딕", 1))
        label_line.place(x=10, y=120)

        #세로 스크롤바 생성
        scroll_y = Scrollbar(self.win, orient=VERTICAL)
        scroll_y.place(x=375, y=128, width=14, height=355)
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
        self.Product_Check()
        
        #데이터 삽입
        for i in range(len(self.result)):
            self.treeview.insert("", "end", text=i+1, values=self.result[i], iid=str(i))


        self.treeview.bind('<ButtonRelease-1>', self.click_item)
        self.win.mainloop()

#op = Order_PAN()
#op.Order_PAN_Call()