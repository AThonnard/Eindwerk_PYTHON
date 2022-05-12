################################ MAIN LOGIN PAGE ##################################
# This page is the main login page from the website FC SYNTRA                     #
# User logs in with login username & password                                     #
# User can choose his/her profile: supporter or administrator                     #
# There is a link if user does not remember the password (will not be created)    #
# If user logs in for the first time, he/she can create a login ==> another page  #
###################################################################################

from tkinter import *
from tkinter.ttk import Combobox

#COMMAND CONNECT
def connect():
    return

# creation page Main_Login_Page
login_page = Tk()
login_page.title("FC Syntra Genk")
login_page.state("zoomed")
login_page.config(bg='DodgerBlue3')
login_page.grid_rowconfigure(0, weight=1)
login_page.grid_columnconfigure(0, weight=1)

# #Logo
# my_image = PhotoImage(file="logo.png")
# Label(login_page,image=my_image, width="200", height="200").pack()

# TITLE PAGE
L_Title = Label(login_page, text= "FC Syntra", fg='White', bg ='DodgerBlue3', font=('Helvetica',80))
L_Title.pack(pady = 20)

## CANVAS
# CANVAS: kader voor lijnen
my_canvas = Canvas(login_page, width=1224, height=800, background="DodgerBlue2",highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx= 5, pady = 90)

# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="SteelBlue2", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="RoyalBlue4", width=8)

## LABELS

Login = Label(text="LOGIN:", bg= "DodgerBlue3", fg ="White", font=('Helvetica',15) )
Login.place(x = 270 , y = 300)

Password = Label(text="PASSWORD:",bg= "DodgerBlue3", fg ="White", font=('Helvetica',15))
Password.place(x = 220 , y = 400)

Profile = Label(text="PROFIEL:",bg= "DodgerBlue3", fg ="White", font=('Helvetica',15))
Profile.place(x = 245 , y = 500)

Password_forget = Label(text="Paswoord vergeten?", bg = "DodgerBlue2", fg ="White", font=('Helvetica',10))
Password_forget.place(x = 400 , y = 645)

Login_creation = Label(text="Nog geen login? Klik hier.", bg="DodgerBlue2", fg="White",font=('Helvetica',20, 'bold','underline'))
Login_creation.place(x = 400 , y = 700)

## TEKSTVAKKEN
login = StringVar
password = StringVar

login_entry = Entry(textvariable= login, width="50", highlightthickness=2)
login_entry.place(x = 400 , y = 300, height = "30")

password_entry = Entry(textvariable= password, width="50",highlightthickness=2)
password_entry.place(x = 400 , y = 400, height = "30")

#Combobox Profiel kiezen
v_profile = [" ", "Supporter", "Administrator"]
profile = Combobox(login_page, values = v_profile, width="47")
profile.place(x = 400 , y = 500, height = "30")

#BUTTON CONNECT
login_button =Button(login_page, text="Connect", width="30", command= connect, bg ="White")
login_button.place(x = 400 , y = 600, height = "30")

login_page.mainloop()
