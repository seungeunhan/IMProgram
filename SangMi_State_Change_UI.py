from tkinter import *
import tkinter as tk
from tkinter import ttk as ttk
from PIL import Image, ImageTk
from SangMi_Helper_Class import SangMi_Helper

#Helper = SangMi_Helper()
#ImmList,notImmList,ImmList_ch = Helper.IMMSangMi_List("All")

class SanMi_state_change_UI:
    helper = SangMi_Helper()
    imlst = []
    imlst = helper.imbak_lst_call()

    def gui(self):
        sangmi_state_change_page = tk.Tk()
        style = ttk.Style()

        sangmi_state_change_page.title("A TWOSOME PLACE_상미_상태변경")

        width = 500
        height = 350
        screen_width = sangmi_state_change_page.winfo_screenwidth()
        screen_height = sangmi_state_change_page.winfo_screenheight()
        sangmi_state_change_page.resizable(False, False)

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        sangmi_state_change_page.geometry('%dx%d+%d+%d' % (width, height, x+300, y-150))



        #회색 테두리
        grayborder = Frame(sangmi_state_change_page,width=484,height=224,background="#BFBFBF")
        grayborder.place(x=8,y=58)
        #흰색배경
        sangmi_info = Frame(sangmi_state_change_page, width=480, height=220, background="white")
        sangmi_info.place(x=10, y=60)

        # 버튼 생성
        button1 = tk.Button(sangmi_state_change_page, text="폐  기",bg="#C7CBB1", fg='black', anchor='center', font=('맑은 고딕', 12, 'bold'))
        button1.place(x=40, y=290, width=200, height=45)
        # 버튼 생성
        button2 = tk.Button(sangmi_state_change_page, text="사용 완료",bg="#C7CBB1", fg='black', anchor='center', font=('맑은 고딕', 12, 'bold'))
        button2.place(x=260, y=290, width=200, height=45)

        #트리뷰 생성
        column = ["No", "제품명", "상미기간",  "상미종료일", "상태"]
        treeview = ttk.Treeview(sangmi_state_change_page, columns=column)
        treeview.place(x=10, y=60, width=480 , height=220)

        #스크롤바
        scroll_y = Scrollbar(sangmi_state_change_page  , orient=VERTICAL)
        scroll_y.place(x=470, y=60, width=20, height=220)
        treeview.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=treeview.yview)


        #컬럼 컬럼명, 넓이, 정렬

        treeview.column("#0", width=40, anchor="center", stretch=False)
        treeview.heading("#0", text="No", anchor="center")
        treeview.column("#1", width=150, anchor="center", stretch=False)
        treeview.heading("#1", text="제품명", anchor="center")
        treeview.column("#2", width=60, anchor="center", stretch=False)
        treeview.heading("#2", text="상미기간", anchor="center")
        treeview.column("#3", width=150, anchor="center", stretch=False)
        treeview.heading("#3", text="상미 종료 날짜", anchor="center")
        treeview.column("#4", width=60, anchor="center", stretch=False)
        treeview.heading("#4", text="상태", anchor="center")

        
        #데이터 삽입
        num=0
        for i in range(len(self.imlst)):
            treeview.insert("", "end", text=num+1, values=self.imlst[i],tags='red')
            num=num+1


        sangmi_state_change_page.mainloop()


