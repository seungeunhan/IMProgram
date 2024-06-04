from tkinter import *
import tkinter as tk
from MainUI import MainUi

class Login :
    login_data = ['1','1','1']

    def button_clicked(self):
        en_value = self.text_cp.get()
        id_value = self.text_id.get()
        pw_value = self.text_pw.get()
        
        if en_value != self.login_data[0]:
            print('en불허')
        elif id_value != self.login_data[1]:
            print('id불허')
        elif pw_value != self.login_data[2]:
            print('pw불허')
        else:
            print('통과')
            self.win.destroy()
            ma = MainUi()
            ma.MainUi_Call()




#<GUI 구현부>-------------------------------------------------------------------

    def login(self):
        self.win = tk.Tk()
        self.win.title("투썸 재고 관리 시스템")  # 창 제목
        # 창 넓이, 높이 사이즈
        width = 800
        height = 550
        
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        self.win.resizable(False,False)

        # 창 위치 계산
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.win.geometry('%dx%d+%d+%d' % (width, height, x, y))

        #프레임
        all_Frame = Frame(self.win, width=800, height=550)          
        all_Frame.place(x=0,y=0)

        #창 아이콘 설정
        ico = tk.PhotoImage(file='image_zip/twosomelogo.png')
        self.win.iconphoto(False, ico)

        #창 백그라운드 이미지
        img = tk.PhotoImage(file='image_zip/login_bg.png')
        bg_label =  tk.Label(self.win, image=img)
        bg_label.pack()


        #캔버스와 텍스트
        canvas = tk.Canvas(self.win, width=350, height=400, background='white')
        canvas.place(x=210, y=70)

        canvas.create_text(175,360,text="비밀번호를 잊으셨나요?",fill="black",font=("맑은 고딕",9,"underline"))

        #투썸 로고 이미지
        photo = PhotoImage(file="image_zip/twosomelogo1.png")
        pLabel = Label(self.win, image=photo, borderwidth=0, bg="white")
        pLabel.place(x=260, y=90)

        #버튼 만들기(첫째줄)
        btn_login = tk.Button(self.win, text="로그인", justify="center",width=25, height=1,bg="#474747",relief="flat",borderwidth="1",font=("맑은 고딕",12),foreground="white", command=self.button_clicked)
        btn_login.place(x=270,y=370)


        #텍스트 박스(entry)(회사 코드)
        canvas.create_text(60,120,text="회사코드",fill="black",font=("맑은 고딕",10))
        self.text_cp = tk.Entry(self.win, width=19, font=("맑은 고딕",14), borderwidth=1, foreground="#333333")
        self.text_cp.place(x= 330, y= 174)

        #텍스트 박스(entry)(아이디)
        canvas.create_text(60,190,text="아이디",fill="black",font=("맑은 고딕",10))
        self.text_id = tk.Entry(self.win, width=19, font=("맑은 고딕",14), borderwidth=1, foreground="#333333")
        self.text_id.place(x= 330, y= 238)

        #텍스트 박스(entry)(비밀번호)
        canvas.create_text(60,250,text="비밀번호",fill="black",font=("맑은 고딕",10))
        self.text_pw = tk.Entry(self.win, width=19, font=("맑은 고딕",14), borderwidth=1, foreground="#333333", show="*")
        self.text_pw.place(x= 330, y= 302)


        self.win.mainloop()


lg = Login()
lg.login()