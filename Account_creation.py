######################## ACCOUNT CREATION PAGE #######################
# This page is the account creation page from the website FC SYNTRA. #
# If the user doesn't have a account, from the main login page there #
# is a link to this page in order to create his login.               #
######################################################################
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
from ttkwidgets.autocomplete import AutocompleteCombobox
import re

#CONNECT TO DATABASE FCSYNTRA
fcsyntra_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "fcsyntra")

mycursor = fcsyntra_db.cursor()

#METHOD OM NAAR MAIN LOGIN PAGINA TE GAAN
def terug_login_pagina():
    create_acc_page.destroy()
    import main_login_page

#PASSWORD CONDITIONS
# Should have at least one number.
# Should have at least one uppercase and one lowercase character.
# Should have at least one special symbol.
# Should be between 6 to 20 characters long.
def check_password():
    passwd = password_entry.get()
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    # compiling regex
    pat = re.compile(reg)
    # searching regex
    mat = re.search(pat, passwd)
    # validating conditions
    if mat:
        messagebox.showinfo("", "Paswoord is geldig")
    else:
        messagebox.showinfo("","Paswoord is niet geldig! Het voldoet niet aan de voorwaarden: \n"
                               "Het moet minstens 1 cijfer bevatten.\nEr moet minstens 1 hoofdletter zijn.\n"
                               "Er moet minstens 1 speciaal teken hebben.\nHet moet tussen de 6 en 20 karakters lang zijn")

def encrypt_pwd():
    global encpwd
    global pwd_key
    pwd = password_entry.get()
    print(pwd)
    pwd_key = Fernet.generate_key()
    print(pwd_key)
    f = Fernet(pwd_key)
    encpwd = f.encrypt(pwd.encode())
    print(encpwd)

#NAKIJKEN INGEBRACHTE GEGEVENS EN WEGSCHRIJVEN IN DATABASE
def validate_data():
    lijst_data = [firstname_entry.get(),lastname_entry.get(),
                  email_entry.get(),country_cb.get(),
                  postal_entry.get(), state_entry.get(),
                  street_entry.get(), phone_entry.get(),
                  title_cb.get(),language_cb.get(),
                  password_entry.get(),password_repeat_entry.get()]
    teller = 0
    for x in lijst_data:
        if len(x) > 0:
            teller = teller+1
    if teller < 12:
        messagebox.showinfo("", "U heeft niet alle verplichte velden ingevuld")
    elif (teller == 12) and (conditions_check.get() == 0):
        messagebox.showinfo("", "U moet de algemene voorwaarden aanvaarden")
    elif (teller == 12) and (conditions_check.get() == 1):
        sql = "INSERT INTO leden (voornaam, achternaam, email, land, postcode, gemeente, straat, telefoon,gsm,aanspreking,taal, paswoord, pwd_key) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = [firstname_entry.get(),lastname_entry.get(),
                  email_entry.get(),country_cb.get(),
                  postal_entry.get(), state_entry.get(),
                  street_entry.get(), phone_entry.get(), mobile_entry.get(),
                  title_cb.get(),language_cb.get(),
                  encpwd,pwd_key]
        mycursor.execute(sql,val)
        fcsyntra_db.commit()
        messagebox.showinfo("", "Account succesvol gecreëerd")
        create_acc_page.destroy()
    return

#MAIN FUNCTIE WANNEER KNOP 'VALIDEER GEGEVENS' WORDT INGEDRUKT
def main_check_data():
    if password_entry.get() == password_repeat_entry.get():   #VERIFICATIE OF 2 PASWOORDEN IDENTIEK ZIJN
        check_password()                                      #VOORWAARDEN PASWOORD CHECK
        encrypt_pwd()                                         #ENCRYPTIE PASWOORD IN DATABASE
        validate_data()                                       #VALIDEREN VAN GEGEVENS: NAKIJKEN OF ALLES IS INGEVULD EN DAN WEGSCHRIJVEN NAAR DB
    else:
        messagebox.showinfo("", "Beide paswoorden zijn NIET identiek")

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

firstname_l = Label(text="Voornaam", bg= "DodgerBlue3", fg ="White", font=('Helvetica',12) )
firstname_l.place(x = 245 , y = 210)

lastname_l = Label(text="Familienaam",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
lastname_l.place(x = 225 , y = 260)

email_l = Label(text="Mail adres",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
email_l.place(x = 245 , y = 310)

country_l = Label(text="Land",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
country_l.place(x = 280 , y = 360)

postal_l = Label(text="Postcode + Gemeente",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
postal_l.place(x = 160 , y = 410)

street_l = Label(text="Straat",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
street_l.place(x = 270 , y = 460)

phone_number_l = Label(text="Telefoonnummer",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
phone_number_l.place(x = 200 , y = 510)

title = Label(text="Aanspreking",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
title.place(x = 230 , y = 560)

language_l = Label(text="Taal",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
language_l.place(x = 280 , y = 610)

title_password_l = Label(text="UW PASWOORD",bg= "DodgerBlue3", fg ="White", font=('Helvetica',20, "bold"))
title_password_l.place(x = 90 , y = 670)

password_label = Label(text="Paswoord",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
password_label.place(x = 250 , y = 720)

password_repeat_label = Label(text="Herhaal paswoord",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
password_repeat_label.place(x = 200 , y = 770)

mailing_label = Label(text="Hou mij op de hoogte!",bg= "DodgerBlue3", fg ="White", font=('Helvetica',12))
mailing_label.place(x = 180 , y = 820)

inschrijven_label = Label(text="Inschrijven",bg= "DodgerBlue2", fg ="White", font=('Helvetica',12))
inschrijven_label.place(x = 400 , y = 820)

voorwaarden_label = Label(text="Ik aanvaard de algemene voorwaarden",bg= "DodgerBlue2", fg ="White", font=('Helvetica',12))
voorwaarden_label.place(x = 400 , y = 870)

terug_naar_login = Label(text=" << Terug naar login pagina",bg="DodgerBlue3", fg="White",font=('Helvetica',12))
terug_naar_login.place(x = 850 , y = 980)
terug_naar_login.bind("<Button-1>", lambda y:terug_login_pagina())

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
info_check = IntVar(create_acc_page)
conditions_check = IntVar(create_acc_page)

#FIRSTNAME
firstname_entry = Entry(width=50, highlightthickness=2)
firstname_entry.place(x = 370 , y = 210, height = 30)
#LASTNAME
lastname_entry = Entry(width=50,highlightthickness=2)
lastname_entry.place(x = 370 , y = 260, height = 30)
#EMAIL
email_entry = Entry(width=50, highlightthickness=2)
email_entry.place(x = 370 , y = 310, height = 30)
#COUNTRY
country_cb = AutocompleteCombobox(create_acc_page, state = "readonly", width=30)
country_cb['values'] = ('Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe')
country_cb.place(x = 370 , y = 360, height = 30)
#POSTALCODE
postal_entry = Entry( width=10, highlightthickness=2)
postal_entry.place(x = 370 , y = 410, height = 30)
#GEMEENTE
state_entry = Entry(width=45, highlightthickness=2)
state_entry.place(x = 450 , y = 410, height = 30)
#STREET
street_entry = Entry(width=50, highlightthickness=2)
street_entry.place(x = 370 , y = 460, height = 30)
#PHONE NUMBER
phone_entry = Entry(width=30, highlightthickness=2)
phone_entry.place(x = 370 , y = 510, height = 30)
#MOBILE
mobile_entry = Entry( width=30, highlightthickness=2)
mobile_entry.insert(END, "Mobiel (optioneel)")
mobile_entry.place(x = 600 , y = 510, height = 30)
#TITLE
title_cb = Combobox(create_acc_page,state = "readonly", width=10)
title_cb['values'] = ('Dhr', 'Mevr.')
title_cb.place(x = 370 , y = 560, height = 30)
#LANGUAGE
language_cb = Combobox(state = "readonly",width=20)
language_cb['values']=('Nederlands', 'Frans', 'Duits','Engels')
language_cb.place(x = 370 , y = 610, height = 30)
#PASSWORD
password_entry = Entry(width=30, highlightthickness=2)
password_entry.place(x = 370 , y = 720, height = 30)
#PASSWORD REPEAT
password_repeat_entry = Entry(show="*", width=30, highlightthickness=2)
password_repeat_entry.place(x = 370 , y = 770, height = 30)
#CHECK BOX INSCHRIJVEN
info_check_box = Checkbutton(create_acc_page, variable=info_check, onvalue=1, offvalue=0, bg="DodgerBlue2",highlightthickness=2)
info_check_box.place(x = 370, y = 820)
#CHECK BOX VOORWAARDEN
conditions_checkb = Checkbutton(create_acc_page, variable=conditions_check, onvalue=1, offvalue=0, bg="DodgerBlue2",highlightthickness=2)
conditions_checkb.place(x = 370, y = 870)
#BUTTON CONNECT
login_button =Button(create_acc_page, text="Valideer gegevens", width="30", command= main_check_data, bg ="White")
login_button.place(x = 840 , y = 940, height = "30")

create_acc_page.mainloop()
