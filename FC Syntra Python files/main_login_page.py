############################### MAIN LOGIN PAGE #################################
# This page is the main login page from the website FC SYNTRA                   #
# User logs in with login username & password                                   #
# User can choose his/her profile: supporter or administrator                   #
# There is a link if user does not remember the password (will not be created)  #
# If user logs in for the first time, he/she can create a login ==> another page#
#################################################################################
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
from cryptography.fernet import Fernet

#CONNECT TO DATABASE FCSYNTRA
fcsyntra_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "fcsyntra")

mycursor = fcsyntra_db.cursor()

#VERIFY LOGIN in DB
def login_verify():
    username = username_entry.get()         #Neem ingegeven username
    password = password_entry.get()         #Neem ingegeven paswoord
    profile = profile_entry.get()           #Neem aangevinkte profiel
    decrypt_pwd()                           #paswoord wordt op basis van username gedecrypteerd vanuit database om check te maken met ingebrachte paswoord
    if username == "" or password == "" or profile =="":        #er moet altijd iets ingebracht worden
        messagebox.showinfo("", "Blanks not allowed")
    else:
        if profile == 'Administrator':          #Indien Admin, gaat in database kijken naar Tabel Admin
            sql = f"SELECT email from admin WHERE email = '{username}' AND paswoord = '{password}';"
            mycursor.execute(sql)
            if mycursor.fetchall():
                messagebox.showinfo("", "Login Successful")
                login_page.destroy()
                import admin_page               #Indien verificatie OK is, gaat Admin Pagina open
            else:
                messagebox.showinfo("", "Incorrect Username and/or Password and/or profile")
        elif (profile == 'Supporter'):          #Indien supporter, gaat in database kijken naar Tabel leden
            sql = f"SELECT email from leden WHERE email = '{username}';"
            mycursor.execute(sql)
            if mycursor.fetchall():
                if password == str_decrypted_pwd:       #hier wordt gekeken naar match ingebrachte paswoord en decrypted paswoord
                    messagebox.showinfo("", "Login Successful")
                    get_id_supp()                       #Als ok is, dan gaan we lidnr nemen en wegschrijven in txt file
                    login_page.destroy()
                    import ticket_page                  #men komt dan op pagina bestellen ticket
                else:
                    messagebox.showinfo("", "Incorrect Username and/or Password and/or profile")
            else:
                messagebox.showinfo("", "Incorrect Username and/or Password and/or profile")
        else:
            messagebox.showinfo("", "Incorrect Username and/or Password and/or profile")

#functie om paswoord te decrypten
def decrypt_pwd():
    global str_decrypted_pwd
    username = username_entry.get()
    sql = f"SELECT paswoord, pwd_key from leden WHERE email = '{username}';"
    mycursor.execute(sql)
    for x in mycursor:
        encrypted_pwd = x[0]
        read_key = x[1]
        key = read_key
        f = Fernet(key)
        decrypted_pwd = f.decrypt(encrypted_pwd)
        str_decrypted_pwd = decrypted_pwd.decode('UTF-8')
        print('readed key is ', read_key)
        print('read encrypt pwd = ', encrypted_pwd)
        print("decrypted pwd is ", decrypted_pwd)
        print(str_decrypted_pwd)

#functie om ID lidnr te halen van supporter die aanlogt en die wordt weggeschreven in txt file zodat men in
#pagina ticket bestelling weet wie een bestelling plaatst
def get_id_supp():
    global lidNummer
    username = username_entry.get()
    sql = f"SELECT lidNummer from leden WHERE email = '{username}';"
    mycursor.execute(sql)
    for x in mycursor:
        lidNummer = x[0]
        print(lidNummer)
        Lidnr_log = open("Lidnr_log.txt", "w")
        Lidnr_log.writelines(str(lidNummer))
        Lidnr_log.close()

#functie die pagina opent 'Paswoord vergeten'
def open_reset_pwd_page():
    login_page.destroy()
    import reset_password_page

#functie die pagina opent 'creatie account'
def open_creation_page():
    login_page.destroy()
    import account_creation_page


######################################################################### PAGE CREATIE #############################################################################################

# creation page Main_Login_Page
login_page = Tk()
login_page.title("FC Syntra")
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
Password_forget.bind("<Button-1>", lambda x:open_reset_pwd_page())

Login_creation = Label(text="Nog geen account? Klik hier",bg="DodgerBlue2", fg="White",font=('Helvetica',15, 'bold','underline'))
Login_creation.place(x = 400 , y = 700)
Login_creation.bind("<Button-1>", lambda y:open_creation_page())

## TEKSTVAKKEN ##
username = StringVar
password = StringVar

#LOGIN
username_entry = Entry(width=35, highlightthickness=2, font=20)
username_entry.place(x = 400 , y = 300, height = 30)
#PASSWORD
password_entry = Entry(width=35,show="*", highlightthickness=2, font=20)
password_entry.place(x = 400 , y = 400, height = 30)
#PROFILE
values_profile = [" ", "Supporter", "Administrator"]
profile_entry = Combobox(width=35,values = values_profile, font=20)
profile_entry.place(x = 400 , y = 500, height = 30)

#BUTTON CONNECT
login_button =Button(login_page, text="Connect", width="30", command= login_verify, bg ="White")
login_button.place(x = 400 , y = 600, height = "30")

login_page.mainloop()
