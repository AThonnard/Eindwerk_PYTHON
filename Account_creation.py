######################## ACCOUNT CREATION PAGE #######################
# This page is the account creation page from the website FC SYNTRA. #
# If the user doesn't have a account, from the main login page there #
# is a link to this page in order to create his login.               #
######################################################################
import webbrowser
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image

def validate_data():
    return

# creation page Create Account Page

create_acc_page = Tk()
create_acc_page.title("FC Syntra Genk")
create_acc_page.state("zoomed")
create_acc_page.config(bg='DodgerBlue3')
create_acc_page.grid_rowconfigure(0, weight=1)
create_acc_page.grid_columnconfigure(0, weight=1)

# TITLE PAGE
L_Title = Label(create_acc_page, text= "FC Syntra - Aanmaak Account", fg='White', bg ='DodgerBlue3', font=('Helvetica',40))
L_Title.pack(pady = 20)

#LOGO
my_logo = Image.open("syntrapxl_academie_logo_digitaal_rgb_square.png")
resized = my_logo.resize((200,200), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
new_logo_label = Label(create_acc_page, image=new_logo, bg ="DodgerBlue3")
new_logo_label.place(x=1510, y=45)

## CANVAS ##
# CANVAS: kader voor lijnen
my_canvas = Canvas(create_acc_page, width=1224, height=800, background="DodgerBlue2",highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx= 5, pady = 90)

# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="Red", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="Black", width=8)

## LABELS ##

mandatory_f_label = Label(text="( Alle velden zijn verplicht, tenzij anders vermeld )", bg= "DodgerBlue3", fg ="White", font=('Helvetica',10) )
mandatory_f_label.place(x = 350 , y = 170)

firstname = Label(text="Voornaam", bg= "DodgerBlue3", fg ="White", font=('Helvetica',12) )
firstname.place(x = 245 , y = 210)

lastname = Label(text="Familienaam",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
lastname.place(x = 225 , y = 260)

email = Label(text="Mail adres",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
email.place(x = 245 , y = 310)

country = Label(text="Land",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
country.place(x = 280 , y = 360)

postal = Label(text="Postcode + Gemeente",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
postal.place(x = 160 , y = 410)

street = Label(text="Straat",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
street.place(x = 270 , y = 460)

phone_number = Label(text="Telefoonnummer",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
phone_number.place(x = 200 , y = 510)

title = Label(text="Aanspreking",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
title.place(x = 230 , y = 560)

language = Label(text="Taal",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
language.place(x = 280 , y = 610)

title_password = Label(text="UW PASWOORD",bg= "DodgerBlue3", fg ="White", font=('Helvetica',20, "bold"))
title_password.place(x = 90 , y = 670)

password_label = Label(text="Paswoord",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
password_label.place(x = 250 , y = 720)

password_repeat_label = Label(text="Herhaal paswoord",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
password_repeat_label.place(x = 200 , y = 770)

mailing_label = Label(text="Hou mij op de hoogte",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
mailing_label.place(x = 180 , y = 820)

## TEKSTVAKKEN ##
voornaam = StringVar
familienaam = StringVar
email = StringVar
land = StringVar
postcode = StringVar
gemeente = StringVar
straat = StringVar
telefoon = StringVar
gsm = StringVar
aanspreking = StringVar
taal = StringVar
paswoord = StringVar
paswoordherhaald = StringVar
info_check = IntVar

#FIRSTNAME
firstname_entry = Entry(textvariable = voornaam, width=50, highlightthickness=2)
firstname_entry.place(x = 370 , y = 210, height = 30)
#LASTNAME
lastname_entry = Entry(create_acc_page,textvariable= familienaam, show="*", width="50",highlightthickness=2)
lastname_entry.place(x = 370 , y = 260, height = 30)
#EMAIL
email_entry = Entry(textvariable = email, width=50, highlightthickness=2)
email_entry.place(x = 370 , y = 310, height = 30)
#COUNTRY
country_entry = Entry(textvariable = land, width=30, highlightthickness=2)
country_entry.place(x = 370 , y = 360, height = 30)
#POSTALCODE
postal_entry = Entry(textvariable = postcode, width=10, highlightthickness=2)
postal_entry.place(x = 370 , y = 410, height = 30)
#GEMEENTE
state_entry = Entry(textvariable = gemeente, width=45, highlightthickness=2)
state_entry.place(x = 450 , y = 410, height = 30)
#STREET
street_entry = Entry(textvariable = straat, width=50, highlightthickness=2)
street_entry.place(x = 370 , y = 460, height = 30)
#PHONE NUMBER
phone_entry = Entry(textvariable = telefoon, width=20, highlightthickness=2)
phone_entry.place(x = 370 , y = 510, height = 30)
#MOBILE
mobile_entry = Entry(text ="Optional",textvariable = gsm, width=20, highlightthickness=2)
mobile_entry.place(x = 520 , y = 510, height = 30)
#TITLE
title_entry = Entry(textvariable = aanspreking, width=10, highlightthickness=2)
title_entry.place(x = 370 , y = 560, height = 30)
#LANGUAGE
language_entry = Entry(textvariable = taal, width=20, highlightthickness=2)
language_entry.place(x = 370 , y = 610, height = 30)
#PASSWORD
password_entry = Entry(textvariable = paswoord, width=30, highlightthickness=2)
password_entry.place(x = 370 , y = 720, height = 30)
#PASSWORD REPEAT
password_repeat_entry = Entry(textvariable = paswoordherhaald, width=30, highlightthickness=2)
password_repeat_entry.place(x = 370 , y = 770, height = 30)

#BUTTON CONNECT
login_button =Button(create_acc_page, text="Valideer gegevens", width="30", command= validate_data, bg ="White")
login_button.place(x = 840 , y = 940, height = "30")

#CHECK BOX INFO
info_check_box = Checkbutton(create_acc_page, variable=info_check, onvalue=1, offvalue=0, bg="DodgerBlue2",highlightthickness=2)
info_check_box.place(x = 370, y = 820)

create_acc_page.mainloop()
