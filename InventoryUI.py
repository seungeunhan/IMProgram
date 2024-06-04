from tkinter import *
import tkinter as tk
import tkinter.ttk
from tkinter import ttk
from InventoryHelperclass import InventoryHelper

class InventoryUI:
    Helper = InventoryHelper()
    #트리뷰 생성// 각 카테고리에서 List를 받아 해당 Frame에 출력
    def CheckList(self,category,Framename):

        #출력할 임박/임박아님 리스트 불러오기
        immList, notimmList = self.Helper.getInventoryList(category)

        #테두리 회색
        bordergray1 = Label(Framename,width=131,height=27,background="#AFABAB").place(x=20,y=93)

        #트리뷰
        column=["체크","제품번호","제품명","재고량","유통기한"]   #컬럼명
        treeview=tkinter.ttk.Treeview(Framename, columns=column)  #트리뷰 생성
        treeview.place(x=20, y=100, height=400, width=915)  #표 위치, 사이즈

        scroll_y = Scrollbar(Framename, orient=VERTICAL)
        scroll_y.place(x=920, y=100, width=22, height=400)
        treeview.configure(yscrollcommand=scroll_y.set)
        treeview.tag_configure("imm",background="#FF7975")
        scroll_y.configure(command=treeview.yview)

        #컬럼 컬럼명, 넓이, 정렬
        treeview.column("#0", width=40,anchor="center",stretch=False)
        treeview.heading("#0", text="No",anchor="center")
        treeview.column("#1", width=200,anchor="center",stretch=False)
        treeview.heading("#1", text="제품번호",anchor="center")
        treeview.column("#2", width=290,anchor="center",stretch=False)
        treeview.heading("#2", text="제품명",anchor="center")
        treeview.column("#3", width=90,anchor="center",stretch=False)
        treeview.heading("#3", text="재고량",anchor="center")
        treeview.column("#4", width=250,anchor="center",stretch=False)
        treeview.heading("#4", text="유통기한",anchor="center")

        #데이터 삽입
        num=0
        for i in range(len(immList)):
            treeview.insert("", "end", text=num+1, values=immList[i],tags='imm')
            num=num+1

        for i in range(len(notimmList)):
            treeview.insert("", "end", text=num+1, values=notimmList[i],tags='tag')
            num=num+1

        return 

    #검색 버튼 기능
    def SearchButtonClick(Findword):
        return 

    #수정 버튼 기능
    def UpdateButtonClick():
        return

    #삭제 버튼 기능
    def DelButtonClick():
        return

    #재고창 출력
    def ShowInventory(self):

        InvenPage = tk.Toplevel()
        style = ttk.Style()

        InvenPage.title("A TWOSOME PLACE_재고")

        width = 1000
        height = 700

        screen_width = InvenPage.winfo_screenwidth()
        screen_height = InvenPage.winfo_screenheight()
        InvenPage.resizable(False,False)

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        InvenPage.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #창 백그라운드 색상
        InvenPage.configure(bg='#F5F5F5')

        #창 아이콘 설정 
        ico = tk.PhotoImage(file='image_zip/twosomelogo.png')
        InvenPage.iconphoto(False, ico)

        # 투썸로고 이미지
        logo_img = PhotoImage(file="image_zip/twosomelogo1.png")
        pLabel = Label(InvenPage, image=logo_img, borderwidth=0, bg="#F5F5F5")
        pLabel.place(x=0, y=25)

        #회색 테두리
        grayborderlabel=Label(InvenPage,bg="#BFBFBF",width=9,height=3)
        grayborderlabel.place(x=17,y=107)

        #재고 탭
        TitleLabel = Label(InvenPage,text="재고",anchor="center",
                        font=("맑은고딕",11),bg="#474747",fg="white",relief="flat",
                        width=7,height=1,highlightcolor="#BFBFBF",highlightthickness=3)
        TitleLabel.place(x=19,y=109)

        #수정 버튼
        update_img_btn = PhotoImage(file="image_zip/수정버튼.png")
        UpdateButton= tk.Button(InvenPage,padx=72,pady=10,image=update_img_btn,relief="groove",borderwidth="0")
        UpdateButton.place(x=875,y=100)

        #삭제 버튼
        del_img_btn = PhotoImage(file="image_zip/삭제버튼.png")
        DelButton= tk.Button(InvenPage,padx=72,pady=10,image=del_img_btn,relief="groove",borderwidth="0")
        DelButton.place(x=930,y=100)

        #회색 테두리
        grayborder = Frame(InvenPage,width=976,height=560,background="#BFBFBF")
        grayborder.place(x=17,y=134)

        #재고 정보 Frame
        Inveninfo = Frame(InvenPage,width=972,height=560,background="white")
        Inveninfo.place(x=19,y=135)

        #상위 카테고리+트리뷰 테마
        style.theme_create("parcate")
        style.theme_settings("parcate",{
            "TNotebook":{"configure":{"tabposition":"n","background":"white","bordercolor":"white"}},
            "TNotebook.Tab":{
                "configure":{"relief":"flat","anchor":"center","width":7,"height":40,
                            "font":["맑은 고딕",19],"background":"white","borderwidth":0,"padding":1},
                "map":{"background":[("selected","#C51254")],
                    "foreground":[("selected","white")]}},
            "Treeview":{
                "configure":{"anchor":"center","rowheight":40,"background":"white",
                            "fieldbackground":"white","foreground":"black","font":["맑은 고딕",11],
                            "borderground":"#AFABAB","wraplength":3},
                "map":{"background":[("selected","#CCE8FF")]}
            },
            "Treeview.Heading":{
                "configure":{"rowheight":10,"font":["맑은 고딕",11],"background":"white"}
            }})
        style.theme_use("parcate")

        #상위 카테고리
        parentcate = ttk.Notebook(Inveninfo,width=970,height=530)
        parentcate.pack()

        #카테고리 바. 
        childcate = Label(InvenPage,width=138,height=3,bg="#484445") #하위 표시
        childcate.place(x=19,y=175)

        #검색버튼
        search_img_btn = PhotoImage(file="image_zip/검색.png")
        SearchButton = tk.Button(InvenPage,image=search_img_btn, padx=10, pady=2,relief="flat",borderwidth="0", bg="white")
        SearchButton.place(x=920,y=235)
    
        #텍스트 박스(entry)(검색)
        text_search= tk.Entry(InvenPage, text="검색",width=20, font=("맑은 고딕",10), borderwidth=2, foreground="#333333")
        text_search.place(x= 765, y=235)
        
        #콤보박스
        sort1=["날짜순", "제품명"]      
        combobox1 = tkinter.ttk.Combobox(InvenPage,values=sort1, state="readonly"
                                        ,width=9,height=5,font=("맑은 고딕",11),justify="center")     
        combobox1.set(sort1[0])               
        combobox1.place(x=580, y=235)

        sort2=["오름차순", "내림차순"]     
        combobox2 = tkinter.ttk.Combobox(InvenPage,values=sort2, state="readonly"
                                        ,width=9,height=5,font=("맑은 고딕",11),justify="center")     
        combobox2.set(sort2[0])          
        combobox2.place(x=673, y=235)    



        #전체 조회 페이지
        ALLPage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("All",ALLPage)

        #커피 조회 페이지
        CoffePage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("커피",CoffePage)

        #음료 조회 페이지
        DrinkPage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("음료",DrinkPage)

        #케이크 조회 페이지
        CakePage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("All",CakePage)

        #델리 조회 페이지
        DellyPage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("델리",DellyPage)

        #MD 조회 페이지
        MDPage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("MD",MDPage)

        #기타 조회 페이지
        OtherPage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("기타",OtherPage)

        #검색 기능 구현하지 않았기 때문에 노출되지 않으며 기능 없습니다.
        #검색 결과 페이지
        SearchPage=Frame(Inveninfo,width=950,height=500,bg="white")
        self.CheckList("검색",SearchPage)

        parentcate.add(ALLPage,text="전체")
        parentcate.add(CoffePage,text="커피")
        parentcate.add(DrinkPage,text="음료")
        parentcate.add(CakePage,text="케이크")
        parentcate.add(DellyPage,text="델리")
        parentcate.add(MDPage,text="MD")
        parentcate.add(OtherPage,text="기타")
        parentcate.add(SearchPage)
        parentcate.hide(SearchPage)

        InvenPage.mainloop()


#iv = InventoryUI()
#iv.ShowInventory()