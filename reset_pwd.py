############################### RESET PASSWORD PAGE #################################
# This page is the reset password page from the website FC SYNTRA                   #
# Page will be displayed when user click on main login page on 'paswoord vergeten   #
#####################################################################################
from tkinter import *
from PIL import ImageTk, Image

#METHOD OM NAAR MAIN LOGIN PAGINA TE GAAN
def terug_login_pagina():
    reset_pwd_page.destroy()
    import main_login_page

def reset_pwd():
    return

# creation page Main_Login_Page
reset_pwd_page = Tk()
reset_pwd_page.title("FC Syntra Genk")
reset_pwd_page.state("zoomed")
reset_pwd_page.config(bg='DodgerBlue3')
reset_pwd_page.grid_rowconfigure(0, weight=1)
reset_pwd_page.grid_columnconfigure(0, weight=1)

# TITLE PAGE
L_Title = Label(reset_pwd_page, text= "FC Syntra - Herstel paswoord", fg='White', bg ='DodgerBlue3', font=('Helvetica',50))
L_Title.pack(pady = 40)

#INFO LABEL ONDER TITEL PAGINA
L_info = Label(reset_pwd_page, text= "Voeg Uw Emailadres In Druk Op ""Herstel Paswoord"". Na Een Paar Minuten Ontvangt U Een Email Met Login Gegevens.", fg='White', bg ='DodgerBlue3', font=('Helvetica',14))
L_info.pack(pady = 30)

#LOGO
my_logo = Image.open("syntrapxl_academie_logo_digitaal_rgb_square.png")
resized = my_logo.resize((200,200), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
new_logo_label = Label(reset_pwd_page, image=new_logo, bg ="DodgerBlue3")
new_logo_label.place(x=1500, y=190)

## CANVAS ##
# CANVAS: kader voor lijnen
my_canvas = Canvas(reset_pwd_page, width=1224, height=800, background="DodgerBlue2",highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx= 5, pady = 90)

# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="Red", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="Black", width=8)

#EMAIL VAK
email_entry = Entry(width=50, highlightthickness=2)
email_entry.place(x = 800 , y =380,height = "30")

#BUTTON CONNECT
reset_button =Button(reset_pwd_page, text="Herstel Paswoord", width="30", command= reset_pwd, bg ="White")
reset_button.place(x = 845 , y = 430, height = "30")

#TERUG MAIN LOGIN PAGE
terug_naar_login = Label(text=" << Terug naar login pagina",bg="DodgerBlue2", fg="White",font=('Helvetica',12))
terug_naar_login.place(x = 845 , y = 470)
terug_naar_login.bind("<Button-1>", lambda y:terug_login_pagina())

reset_pwd_page.mainloop()
