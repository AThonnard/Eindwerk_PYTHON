############################ ADMIN PAGE ##############################
# This page is the admin page from the website FC SYNTRA.            #
# Admins log in to this portal to change reservation or create a new #
# admin. Page is accessed by logging in as administrator on login.   #
######################################################################
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="fcsyntra"
)

mycursor = db.cursor()


def voeg_admin_toe():  # function to add new admin
    lijst_new_admin = [admin_vn_entry.get(), admin_an_entry.get(), admin_email_entry.get(), admin_pw_entry.get()]
    teller = 0
    for x in lijst_new_admin:  # check if all fields are filled in
        if len(x) > 0:
            teller = teller + 1
    if teller < 4:
        messagebox.showinfo("", "U heeft niet alle verplichte velden ingevuld")
    elif teller == 4:
        sql = "INSERT INTO admin (voornaam, achternaam, email, paswoord) VALUES (%s,%s,%s,%s)"
        val = [admin_vn_entry.get(), admin_an_entry.get(), admin_email_entry.get(), admin_pw_entry.get()]
        mycursor.execute(sql, val)
        db.commit()
    return


def delete_reservation():  # function to delete one reservation, determined by filled in infomation
    lijst_delete1 = [vak_entry.get(), rij_entry.get(), stoel_entry.get()]
    d1_teller = 0
    for x in lijst_delete1:  # check if all necessary fields are filled in
        if len(x) > 0:
            d1_teller = d1_teller + 1
    if d1_teller < 3:
        messagebox.showinfo("", "Gelieve vak, rij en stoelnummer in te vullen")
    elif d1_teller == 3:
        sql = "UPDATE stadion SET reserved = 'Nee' WHERE (tribune = %s AND rij = %s AND stoel = %s)"
        val = lijst_delete1
        mycursor.execute(sql, val)
        db.commit()
        display_data()
    return


def delete_all_reservations():  # function to delete all reservations
    sql = "UPDATE stadion SET reserved = 'Nee'"
    mycursor.execute(sql)
    db.commit()
    display_data()
    return


def display_data():  # function to display all reserved seats in the GUI table
    for item in stadion_records.get_children():
        stadion_records.delete(item)
    mycursor.execute("SELECT tribune, rij, stoel, reserved FROM stadion WHERE reserved = 'Ja'")
    result = mycursor.fetchall()
    for row in result:
        stadion_records.insert('', END, values=row)
    return


# TKINTER SETUP
admin_page = Tk()
admin_page.title("FC Syntra Genk")
admin_page.state("zoomed")
admin_page.config(bg='DodgerBlue3')
admin_page.grid_rowconfigure(0, weight=1)
admin_page.grid_columnconfigure(0, weight=1)

# TITLE PAGE
L_Title = Label(admin_page, text="FC Syntra - Admin", fg='White', bg='DodgerBlue3', font=('Helvetica', 40))
L_Title.pack(pady=20)

# LOGO
my_logo = Image.open("syntrapxl_academie_logo_digitaal_rgb_square.png")
resized = my_logo.resize((200, 200), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
new_logo_lbl = Label(admin_page, image=new_logo, bg="DodgerBlue3")
new_logo_lbl.place(x=1500, y=45)

# CANVAS
# CANVAS: kader voor lijnen
my_canvas = Canvas(admin_page, width=1224, height=800, background="DodgerBlue2", highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx=5, pady=90)

# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="red", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="black", width=8)

# LABELS
title1_lbl = Label(text="ENKELE RESERVATIE", bg="DodgerBlue2", fg="White", font=('Helvetica', 20, "bold"))
title1_lbl.place(x=370, y=210)

vak_lbl = Label(text="Vak", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
vak_lbl.place(x=370, y=260)

rij_lbl = Label(text="Rij", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
rij_lbl.place(x=370, y=310)

stoel_lbl = Label(text="Stoel nummer", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
stoel_lbl.place(x=370, y=360)

title2_lbl = Label(text="ALLE RESERVATIES", bg="DodgerBlue2", fg="White", font=('Helvetica', 20, "bold"))
title2_lbl.place(x=370, y=510)

title3_lbl = Label(text="NIEUWE ADMIN", bg="DodgerBlue2", fg="White", font=('Helvetica', 20, "bold"))
title3_lbl.place(x=1000, y=210)

admin_vn_lbl = Label(text="Voornaam", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_vn_lbl.place(x=1000, y=260)

admin_an_lbl = Label(text="Achternaam", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_an_lbl.place(x=1000, y=310)

admin_email_lbl = Label(text="Email", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_email_lbl.place(x=1000, y=360)

admin_pw_lbl = Label(text="Paswoord", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_pw_lbl.place(x=1000, y=410)

# TEKSTVAKKEN
vak = StringVar
rij = StringVar
stoel = StringVar
voornaam = StringVar
achternaam = StringVar
email = StringVar
paswoord = StringVar

vak_entry = Entry(width=10, highlightthickness=2)
vak_entry.place(x=500, y=260, height=30)

rij_entry = Entry(width=10, highlightthickness=2)
rij_entry.place(x=500, y=310, height=30)

stoel_entry = Entry(width=10, highlightthickness=2)
stoel_entry.place(x=500, y=360, height=30)

admin_vn_entry = Entry(width=20, highlightthickness=2)
admin_vn_entry.place(x=1200, y=260, height=30)

admin_an_entry = Entry(width=20, highlightthickness=2)
admin_an_entry.place(x=1200, y=310, height=30)

admin_email_entry = Entry(width=20, highlightthickness=2)
admin_email_entry.place(x=1200, y=360, height=30)

admin_pw_entry = Entry(width=20, highlightthickness=2)
admin_pw_entry.place(x=1200, y=410, height=30)

# BUTTON CONNECT
delete_one_button = Button(text="Verwijder reservatie", width="30", command=delete_reservation, bg="White")
delete_one_button.place(x=370, y=410, height="30")

delete_all_button = Button(text="Verwijder alle reservaties", width="30", command=delete_all_reservations,
                           bg="White")
delete_all_button.place(x=370, y=560, height="30")

add_admin_button = Button(text="Voeg admin toe", width="30", command=voeg_admin_toe, bg="White")
add_admin_button.place(x=1050, y=460, height="30")

# DATA TABLE SETUP
scroll_y = Scrollbar(admin_page, orient=VERTICAL)

stadion_records = ttk.Treeview(admin_page, height=8, columns=("tribune", "rij", "stoel", "reserved"),
                               yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)

stadion_records.heading("tribune", text="Vak")
stadion_records.heading("rij", text="Rij")
stadion_records.heading("stoel", text="Stoel")
stadion_records.heading("reserved", text="Gereserveerd")

stadion_records['show'] = 'headings'

stadion_records.column("tribune", width=50)
stadion_records.column("rij", width=50)
stadion_records.column("stoel", width=50)
stadion_records.column("reserved", width=80)

stadion_records.place(x=650, y=260)
display_data()

# PROGRAM START
admin_page.mainloop()
