from tkinter import *
from PIL import ImageTk, Image
import os
import sys
from functools import partial
import main
import transformation as Trasnform
import connection as finger_scan
import mysql_conn 


def etr2():
    window = Tk()
    ETRPage2(window)
    window.mainloop()


class ETRPage2:

    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Rigester Page')

        p = ""

        self.bg_frame = Image.open(p + r"images\background2.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "التصويت عملية"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=10, width=300, height=50)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open(p + r'images\logo.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=5)

        # ========================================================================
        # ============================Name====================================
        # ========================================================================
        def sel():
            selection = "You selected the option " + str(var.get())
        self.username_label = Label(self.lgn_frame, text="  التسلسل    القائمة     المرشح", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=5, y=80)
        var = IntVar()
        self.username_label2 = Radiobutton(self.lgn_frame,variable=var, value=1, text="1    قائمة1     علي عباس المرشح", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"),command=sel)
        self.username_label2.place(x=5, y=120)
        self.username_label3 = Radiobutton(self.lgn_frame,variable=var, value=2, text="2    قائمة2     علي باسم المرشح", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"),command=sel)
        self.username_label3.place(x=5, y=160)

        self.username_label4 = Radiobutton(self.lgn_frame,variable=var, value=3, text="3    قائمة3     احمد عباس المرشح", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"),command=sel)
        self.username_label4.place(x=5, y=200)
        self.username_label5 = Radiobutton(self.lgn_frame,variable=var, value=3, text="4    قائمة3     محمد عباس المرشح", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"),command=sel)
        self.username_label5.place(x=5, y=240)


        self.search_button = Button(self.lgn_frame, text='ارسال', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                    command="searching2")
        self.search_button.place(x=5, y=370)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')


class ETRPage:

    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Rigester Page')


        p=""


        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open(p+r"images\background2.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Voting"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=10, width=300, height=50)


        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open(p+r'images\logo.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=5)



        # ========================================================================
        # ============================Name====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Search the name:", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=5, y=100)
        Name = StringVar()
        self.name_entry = Entry(self.lgn_frame,textvariable=Name, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.name_entry.place(x=5, y=130, width=270)

        self.name_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.name_line.place(x=5, y=152)


        def searching(name):
            # name = input('Enter the name:')
            myresult = mysql_conn.select_all(name.get())
            

            c = 0


            self.bel = Label(self.lgn_frame, text="id", bg="#040405", fg="white",
                                        font=("yu gothic ui", 13, "bold"))
            self.bel.place(x=400, y=10)

            self.bel2 = Label(self.lgn_frame, text="Name", bg="#040405", fg="white",
                                        font=("yu gothic ui", 13, "bold"))
            self.bel2.place(x=500, y=10)

            for x in myresult:
                c += 1


                self.bel = Label(self.lgn_frame, text=c, bg="#040405", fg="white",
                                 font=("yu gothic ui", 13, "bold"))
                self.bel.place(x=400, y=10 + c*30)
                self.bel2 = Label(self.lgn_frame, text=x[1], bg="#040405", fg="white",
                                  font=("yu gothic ui", 13, "bold"))
                self.bel2.place(x=500, y=10+ c*30)
                # print(x[0], x[1])
                if len(myresult) != 0:
                    self.ageLabel = Label(self.lgn_frame, text="enter the id :", bg="#040405", fg="white",
                                                font=("yu gothic ui", 13, "bold"))
                    self.ageLabel.place(x=5, y=220)
                    id = StringVar()
                    self.ageLabel_entry = Entry(self.lgn_frame, textvariable=id, highlightthickness=0, relief=FLAT,
                                            bg="#040405", fg="#6b6a69",
                                            font=("yu gothic ui ", 12, "bold"))
                    self.ageLabel_entry.place(x=5, y=250, width=270)

                    self.ageLabel_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
                    self.ageLabel_line.place(x=5, y=270)
                    photo_and_finger2 = partial(photo_and_finger, id, myresult)

                    self.id_submit = Button(self.lgn_frame, text='Submit', font=("yu gothic ui", 13, "bold"),
                                                width=25, bd=0,
                                                bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                                command=photo_and_finger2)
                    self.id_submit.place(x=5, y=280)

        def photo_and_finger(id, myresult):
            id = int(id.get())
            name_result = myresult[id - 1][1]
            id = int(myresult[id - 1][0])

            def browseFiles(fname):
                # finger_scan.SCAN(fname) #ارجاع جهاز البصمة
                fname = "finger/" + "a3"  # delete this

                filename = fname + ".bmp"
                self.label_file_explorer = Label(self.lgn_frame, text=filename, bg="#040405", fg="white",
                                                 font=("yu gothic ui", 13, "bold"))
                self.label_file_explorer.place(x=5, y=360)

                def tak_face(name):
                    ff = main.take_face(name)
                    ff = main.take_face(name)
                    self.face_label2 = Label(self.lgn_frame, text="", bg="#040405", fg="white",
                                            font=("yu gothic ui", 13, "bold"))
                    self.face_label2.place(x=5, y=430)

                    if ff:
                        self.face_label2.configure(text=" face in your photo is founded")
                        key = (0.1, 0.1)

                        sending = main.Sender_voting_part(filename, ff, key, name_result + "_voting", id)
                        if (sending):
                            # validateLogin2 = partial(getinfo, Name, age, filename)
                            def subm():
                                strin = Trasnform.send_file("files/" + name_result + '_voting.npz', "localhost", 80)

                                self.send_label = Label(self.lgn_frame, text=strin, bg="#040405", fg="white",
                                                        font=("yu gothic ui", 13, "bold"))
                                self.send_label.place(x=5, y=490)

                                def validateEnter():
                                    # print("username entered :", username.get())
                                    # print("password entered :", password.get())

                                    window.destroy()
                                        # tkWindow.withdraw
                                        # os.startfile(p+r"\GUI.py")
                                    etr2()
                                        # files()

                                def validation():
                                    strinv = mysql_conn.select_con(id, "vt_result")
                                    print("stringenv: ",strinv)
                                    print(strinv,'********************')
                                    stt = "finger score: " + str(strinv[0][3]) + " ,face validation: " + str(
                                        strinv[0][4])
                                    self.send_label2 = Label(self.lgn_frame, text=stt, bg="#040405", fg="white",
                                                            font=("yu gothic ui", 13, "bold"))
                                    self.send_label2.place(x=5, y=560)
                                    validateE = partial(validateEnter)

                                    self.enter_button = Button(self.lgn_frame, text='Enter',
                                                            font=("yu gothic ui", 13, "bold"),
                                                            width=25, bd=0,
                                                            bg='#3047ff', cursor='hand2', activebackground='#3047ff',
                                                            fg='white',
                                                            command=validateE)
                                    self.enter_button.place(x=350, y=520)
                                   
                                self.submitButton = Button(self.lgn_frame, text='get_validation',
                                                           font=("yu gothic ui", 13, "bold"),
                                                           width=25, bd=0,
                                                           bg='#3047ff', cursor='hand2', activebackground='#3047ff',
                                                           fg='white',
                                                           command=validation)
                                self.submitButton.place(x=5, y=520)

                            self.submitButton = Button(self.lgn_frame, text='Submit',
                                               font=("yu gothic ui", 13, "bold"),
                                               width=25, bd=0,
                                               bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                               command=subm)
                            self.submitButton.place(x=5, y=460)

                        print(True)
                    else:
                        self.face_label.configure(text="didn't find faces in your photo try again")

                tak_face2 = partial(tak_face, Name)
                self.face = Button(self.lgn_frame, text='Take face',
                                   font=("yu gothic ui", 13, "bold"),
                                   width=25, bd=0,
                                   bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                   command=tak_face2)
                self.face.place(x=5, y=390)

            # usernameEntry.configure(textvariable=name_result)
            browseFiles2 = partial(browseFiles, name_result)
            self.button_explore = Button(self.lgn_frame, text='Browse Fingerprint file', font=("yu gothic ui", 13, "bold"),
                                    width=25, bd=0,
                                    bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',
                                    command=browseFiles2)
            self.button_explore.place(x=5, y=320)







        searching2 = partial(searching, Name)
        self.search_button = Button(self.lgn_frame, text='Search', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=searching2)
        self.search_button.place(x=5, y=170)



    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')




ccc = "c"

def etr():
    window = Tk()
    ETRPage(window)
    window.mainloop()

class LoginPage:

    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')


        p=""

        def validateLogin(username, password):
            # print("username entered :", username.get())
            # print("password entered :", password.get())
            if (username.get() == "") and (password.get() == ""):
                window.destroy()
                # tkWindow.withdraw
                #os.startfile(p+r"\GUI.py")
                etr()
                # files()
            else:
                return False
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open(p+r"images\background1.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open(p+r'images\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open(p+r'images\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Log In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)
        username = StringVar()
        self.username_entry = Entry(self.lgn_frame,textvariable=username, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open(p+r'images\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)
        password = StringVar()

        self.password_entry = Entry(self.lgn_frame,textvariable=password, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open(p+r'images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file=p+r'images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file=p+r'images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open(p+r'images\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        validateLogin = partial(validateLogin, username, password)

        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=validateLogin)
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file=p+r'images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)



    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()