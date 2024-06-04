from tkinter import *
import tkinter as tk
from tkinter import ttk as ttk
from PIL import Image, ImageTk
from SangMi_Helper_Class import SangMi_Helper
from SangMi_State_Change_UI import SanMi_state_change_UI


Helper = SangMi_Helper()


State_change_ui = SanMi_state_change_UI()


class SangMi_UI:


    def gui_call(self):
        State_change_ui.gui()

    def CheckList(self, category, Framename):

        imlst = []
        notimlst = []
        imlst, notimlst =  Helper.category_lst_call(category)

        #ImmList,notImmList,ImmList_ch = Helper.IMMSangMi_List(category)
        #테두리 회색
        bordergray1 = Label(Framename, width=131, height=27, background="#AFABAB").place(x=20, y=103)
        #트리뷰
        column = ["No", "제품명", "상미기간", "상미 시작 날짜", "상미 종료 날짜", "구 분"]
        treeview = ttk.Treeview(Framename, columns=column)
        treeview.place(x=20, y=110, height=400, width=915)

        treeview.tag_configure("tag2", background="#FF7979")

        scroll_y = Scrollbar(Framename, orient=VERTICAL)
        scroll_y.place(x=920, y=110, width=22, height=400)
        treeview.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=treeview.yview)
        #컬럼 컬럼명, 넓이, 정렬
        treeview.column("#0", width=40, anchor="center", stretch=False)
        treeview.heading("#0", text="No", anchor="center")
        treeview.column("#1", width=250, anchor="center", stretch=False)
        treeview.heading("#1", text="제품명", anchor="center")
        treeview.column("#2", width=70, anchor="center", stretch=False)
        treeview.heading("#2", text="상미기간", anchor="center")
        treeview.column("#3", width=200, anchor="center", stretch=False)
        treeview.heading("#3", text="상미 시작 날짜", anchor="center")
        treeview.column("#4", width=200, anchor="center", stretch=False)
        treeview.heading("#4", text="상미 종료 날짜", anchor="center")
        treeview.column("#5", width=70, anchor="center", stretch=False)
        treeview.heading("#5", text="상태", anchor="center")
        treeview.column("#6", width=70, anchor="center", stretch=False)
        treeview.heading("#6", text="카테고리", anchor="center")

        #데이터 삽입
        #임박 데이터를 우선 삽입 후 임박 아님 데이터를 삽입
        num=0
        for i in range(len(imlst)):
            treeview.insert("", "end", text=num+1, values=imlst[i], tags="tag2")
            num=num+1

        for i in range(len(notimlst)):
            treeview.insert("", "end", text=num+1, values=notimlst[i])
            num=num+1
        return


    def show_SangMi(self):
        sangmi_page = tk.Tk()
        style = ttk.Style()

        sangmi_page.title("A TWOSOME PLACE_상미")

        width = 1000
        height = 700
        screen_width = sangmi_page.winfo_screenwidth()
        screen_height = sangmi_page.winfo_screenheight()
        sangmi_page.resizable(False, False)

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        sangmi_page.geometry('%dx%d+%d+%d' % (width, height, x, y))

        '''
        sangmi_page.configure(bg='#F5F5F5')
        ico = tk.PhotoImage(file='image_zip/twosomelogo.png')
        sangmi_page.iconphoto(False, ico)
        logo_img = PhotoImage(file="image_zip/twosomelogo1.png")
        pLabel = Label(sangmi_page, image=logo_img, borderwidth=0, bg="#F5F5F5")
        pLabel.place(x=0, y=25)
        '''
        #회색 테두리
        grayborderlabel=Label(sangmi_page,bg="#BFBFBF",width=9,height=3)
        grayborderlabel.place(x=17,y=107)
        #상미 탭
        TitleLabel = Label(sangmi_page,text="재고",anchor="center",
                        font=("맑은고딕",11),bg="#474747",fg="white",relief="flat",
                        width=7,height=1,highlightcolor="#BFBFBF",highlightthickness=3)
        TitleLabel.place(x=19,y=109)

        #회색 테두리
        grayborder = Frame(sangmi_page,width=976,height=560,background="#BFBFBF")
        grayborder.place(x=17,y=134)

        sangmi_info = Frame(sangmi_page, width=972, height=560, background="white")
        sangmi_info.place(x=19, y=135)
    
        style.theme_create("parcate")
        style.theme_settings("parcate", {
            "TNotebook": {"configure": {"tabposition": "n", "background": "white", "bordercolor": "white"}},
            "TNotebook.Tab": {
                "configure": {"relief": "flat", "anchor": "center", "width": 7, "height": 40,
                            "font": ["맑은 고딕", 19], "background": "white", "borderwidth": 0, "padding": 1},
                "map": {"background": [("selected", "#C51254")],
                        "foreground": [("selected", "white")]}
            },
            "Treeview": {
                "configure": {"anchor": "center", "rowheight": 40, "background": "white",
                            "fieldbackground": "white", "foreground": "black", "font": ["맑은 고딕", 11],
                            "borderground": "#AFABAB", "wraplength": 3},
                "map": {"background": [("selected", "#CCE8FF")]}
            },
            "Treeview.Heading": {
                "configure": {"rowheight": 10, "font": ["맑은 고딕", 11], "background": "white"}
            }
        })
        style.theme_use("parcate")


        #상위 카테고리
        parentcate = ttk.Notebook(sangmi_info, width=970, height=500)
        parentcate.pack()

        #카테고리 바. 
        childcate = Label(sangmi_page,width=138,height=3,bg="#484445") #하위 표시
        childcate.place(x=19,y=180)

        combo1_var = tk.StringVar()
        combo1_box = ttk.Combobox(sangmi_page, textvariable=combo1_var, width=14, height=5, font=("맑은 고딕", 11))
        combo1_box['values'] = ('날짜순', '제품명순', '구분 상태순', '상미종료기한순')
        combo1_box.current(0)
        combo1_box.place(x=540, y=235)

        combo2_var = tk.StringVar()
        combo2_box = ttk.Combobox(sangmi_page, textvariable=combo2_var, width=9, height=5, font=("맑은 고딕", 12))
        combo2_box['values'] = ('오름차순', '내림차순')
        combo2_box.current(1)
        combo2_box.place(x=673, y=235)
        '''
        #검색버튼
        # 이미지 로드
        image_path = "image_zip/검색.png"
        original_image = Image.open(image_path)

            # 이미지 크기 조정
        resized_image = original_image.resize((int(original_image.width * 1.5), int(original_image.height * 1.5)))
        search_img_btn = ImageTk.PhotoImage(resized_image)

            # 이미지 버튼 생성
        btn_search = tk.Button(sangmi_page, image=search_img_btn, padx=10, pady=2, relief="flat", borderwidth=0, bg="white")
        btn_search.place(x=940, y=235)
        '''

        #텍스트 박스(entry)(검색)
        text_search = tk.Entry(sangmi_page, width=20, font=("맑은 고딕", 10), borderwidth=2, foreground="#333333")
        text_search.place(x=780, y=235)
        text_search.insert(0, "검색")

        # 스타일 생성
        style12 = ttk.Style()
        style12.configure('Custom.TButton', background='gray',foreground="white",anchor='center', font=('맑은 고딕', 12, 'bold'))   

        # 상태변경 버튼
        button1 = ttk.Button(sangmi_page, text="상태 변경", style='Custom.TButton', command=self.gui_call)  
        button1.place(x=880, y=100, width=100, height=30)


        ALLPage = Frame(sangmi_info, width=950, height=500, bg="white")
        self.CheckList("All", ALLPage)

        CoffePage = Frame(sangmi_info, width=950, height=500, bg="white")
        self.CheckList("커피", CoffePage)

        DrinkPage = Frame(sangmi_info, width=950, height=500, bg="white")
        self.CheckList("음료", DrinkPage)

        #기타 조회 페이지
        OtherPage=Frame(sangmi_info,width=950,height=500,bg="white")
        self.CheckList("기타",OtherPage)


        SearchPage = Frame(sangmi_info, width=950, height=500, bg="white")
        self.CheckList("검색", SearchPage)

        notebook = ttk.Notebook(sangmi_info, width=970, height=530)
        notebook.pack()


        parentcate.add(ALLPage,text="전체")
        parentcate.add(CoffePage,text="커피")
        parentcate.add(DrinkPage,text="음료")
        parentcate.add(OtherPage,text="기타")
        parentcate.add(SearchPage)
        parentcate.hide(SearchPage)

        sangmi_page.mainloop()
