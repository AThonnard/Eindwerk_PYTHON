############################### MAIN LOGIN PAGE #################################
# This page is the main login page from the website FC SYNTRA                   #
# User logs in with login username & password                                   #
# User can choose his/her profile: supporter or administrator                   #
# There is a link if user does not remember the password (will not be created)  #
# If user logs in for the first time, he/she can create a login ==> another page#
#################################################################################
import webbrowser
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image

#CONNECT TO DATABASE FCSYNTRA
fcsyntra_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "fcsyntra")

mycursor = fcsyntra_db.cursor()

#VERIFY LOGIN in DB
def login_verify():
    username = username_entry.get()
    password = password_entry.get()
    profile = profile_entry.get()
    if username == "" or password == "" or profile =="":
        messagebox.showinfo("", "Blanks not allowed")
    else:
        if profile == 'Administrator':
            sql = f"SELECT email from admin WHERE email = '{username}' AND paswoord = '{password}';"
            mycursor.execute(sql)
            if mycursor.fetchall():
                messagebox.showinfo("", "Login Successful")
                login_page.destroy()
            else:
                messagebox.showinfo("", "Incorrect Username and/or Password and/or profile")
        else:
            sql = f"SELECT email from leden WHERE email = '{username}' AND paswoord = '{password}';"
            mycursor.execute(sql)
            if mycursor.fetchall():
                messagebox.showinfo("", "Login Successful")
                login_page.destroy()
            else:
                messagebox.showinfo("", "Incorrect Username and/or Password and/or profile")

def open_url_login_vergeten():
    webbrowser.open_new_tab('https://krcgenk.tickethour.be/l0322ww/accountPassword.html')

def open_creation_page():
    login_page.destroy()
    import Account_creation

# creation page Main_Login_Page
login_page = Tk()
login_page.title("FC Syntra Genk")
login_page.state("zoomed")
login_page.config(bg='DodgerBlue3')
login_page.grid_rowconfigure(0, weight=1)
login_page.grid_columnconfigure(0, weight=1)

# TITLE PAGE
L_Title = Label(login_page, text= "FC Syntra", fg='White', bg ='DodgerBlue3', font=('Helvetica',80))
L_Title.pack(pady = 20)

#LOGO
my_logo = Image.open("syntrapxl_academie_logo_digitaal_rgb_square.png")
resized = my_logo.resize((200,200), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
new_logo_label = Label(login_page, image=new_logo, bg ="DodgerBlue3")
new_logo_label.place(x=1500, y=100)

## CANVAS ##
# CANVAS: kader voor lijnen
my_canvas = Canvas(login_page, width=1224, height=800, background="DodgerBlue2",highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx= 5, pady = 90)

# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="Red", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="Black", width=8)

## LABELS ##

Username = Label(text="USERNAME:", bg= "DodgerBlue3", fg ="White", font=('Helvetica',15) )
Username.place(x = 225 , y = 300)

Password = Label(text="PASSWORD:",bg= "DodgerBlue3", fg ="White", font=('Helvetica',15))
Password.place(x = 220 , y = 400)

Profile = Label(text="PROFILE:",bg= "DodgerBlue3", fg ="White", font=('Helvetica',15))
Profile.place(x = 245 , y = 500)

Password_forget = Label(text="Paswoord vergeten?", bg = "DodgerBlue2", fg ="White", font=('Helvetica',10, 'underline'))
Password_forget.place(x = 400 , y = 645)
Password_forget.bind("<Button-1>", lambda x:open_url_login_vergeten())

Login_creation = Label(text="Nog geen account? Klik hier",bg="DodgerBlue2", fg="White",font=('Helvetica',15, 'bold','underline'))
Login_creation.place(x = 400 , y = 700)
Login_creation.bind("<Button-1>", lambda y:open_creation_page())

## TEKSTVAKKEN ##
username = StringVar
password = StringVar

#LOGIN
username_entry = Entry(textvariable = username, width=50, highlightthickness=2)
username_entry.place(x = 400 , y = 300, height = 30)
#PASSWORD
password_entry = Entry(login_page,textvariable= password, show="*", width="50",highlightthickness=2)
password_entry.place(x = 400 , y = 400, height = 30)
#PROFILE
values_profile = [" ", "Supporter", "Administrator"]
profile_entry = Combobox(login_page, values = values_profile, width=47)
profile_entry.place(x = 400 , y = 500, height = 30)

#BUTTON CONNECT
login_button =Button(login_page, text="Connect", width="30", command= login_verify, bg ="White")
login_button.place(x = 400 , y = 600, height = "30")

login_page.mainloop()


