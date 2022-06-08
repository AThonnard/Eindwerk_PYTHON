# ############################## TICKET PAGE ###################################### #
# This page is the ticket page from the website FC SYNTRA                           #
# In this GUI supporters can buy stadion-tickets. Tickets are logged in a database  #
# Supporters can make a selection on tribune, row and chairs.                       #
# Only free chairs are read-in from the db and visualised.                          #
# ################################################################################# #

# get tkinter module
from tkinter import *
from tkinter import messagebox
# get image module
from PIL import ImageTk, Image

# make database connection
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="fcsyntra"
)
mycursor = db.cursor()

# declare lists/variables
naam = ""
options_tribune = []
options_rij = []
options_stoel = []
var_tribune = ""
var_rij = 0
var_stoel = 0

# gets the member-number from the lidn-log.txt file
f = open('Lidnr_log.txt','r')
lidNummer = int(f.read())
f.close()

# gets the member-name from the databank
query = "SELECT voornaam,achternaam FROM leden WHERE lidNummer =%s"
lid = (lidNummer,)
mycursor.execute(query, lid)
myresult = mycursor.fetchall()
for x in myresult:
    naam = x[0] + " " + x[1]

# function test database connection
def toon_database_stadion():
    mycursor.execute("SELECT PlaatsID,tribune,rij,stoel,reserved,prijsTicket FROM stadion")
    for x in mycursor:
        print(x)

# run test database connection
toon_database_stadion()


# function choose tribune
def keuze_tribune():
    # settings text :choose the tribune
    tribune = Label(ticket, text="Kies eerst tribune / vak: ",font=('Helvetica',12))
    tribune.config(bg="DodgerBlue3", fg="white")
    tribune.place(relx="0.09", rely="0.35")

    # gets the free tribune-data from the databank and puts it in a list
    mycursor.execute("SELECT DISTINCT tribune FROM stadion  WHERE reserved = 'Nee'")
    options_tribune = list([x for x, in mycursor])

    # settings optionmenu tribune and command
    tribune_keuze = StringVar()
    tribune_keuze.set("Tribune")
    optionsbox = OptionMenu(ticket, tribune_keuze, *options_tribune,
                            command=keuze_rij) # returns the chosen parameter value_tribune and run function keuze_rij
    optionsbox.place(relx="0.2", rely="0.35")


# function choose row
def keuze_rij(value_tribune):
    # changes the chosen parameter value_tribune to the global variabele var_tribune for the row function
    global var_tribune
    var_tribune = value_tribune

    # gets the free row-data from the chosen tribune from the databank and puts it in a list
    mycursor.execute("SELECT DISTINCT rij FROM stadion WHERE tribune = '" + value_tribune + "' AND reserved = 'Nee'")
    options_rij = list([x for x, in mycursor])

    # settings text choose row
    rij = Label(ticket, text="Kies daarna rij:",font=('Helvetica',12))
    rij.config(bg="DodgerBlue3", fg="white")
    rij.place(relx="0.1", rely="0.45")

    # settings optionbox row and command
    rij_keuze = StringVar()
    rij_keuze.set(options_rij[0])
    optionsbox = OptionMenu(ticket, rij_keuze, *options_rij,
                            command=keuze_stoel) # returns the chosen parameter value_rij and run funct. keuze_stoel
    optionsbox.place(relx="0.2", rely="0.45")

# function choose chair
def keuze_stoel(value_rij):
    # changes the chosen parameter value_rij to the global variabele var_rij for the chair function
    global var_rij
    var_rij = value_rij

    # settings text choose chair
    stoel = Label(ticket, text="Kies daarna stoelnummer:",font=('Helvetica',12))
    stoel.config(bg="DodgerBlue3", fg="white")
    stoel.place(relx="0.07", rely="0.55")

    # gets the free chair-data from the chosen row from the databank and puts it in a list
    query = "SELECT DISTINCT stoel FROM stadion WHERE tribune =%s AND rij=%s AND reserved = 'Nee' ORDER by stoel"
    waarde = (var_tribune, value_rij,)
    mycursor.execute(query, waarde)

    # settings optionmenu choose chair
    options_stoel = list([x for x, in mycursor])
    stoel_keuze = IntVar()
    stoel_keuze.set(options_stoel[0])
    optionsbox = OptionMenu(ticket, stoel_keuze, *options_stoel,command=bevestig_keuze_stoel)
    optionsbox.place(relx="0.2", rely="0.55")

# changes the chosen parameter value_stoel to the global variabele var_stoel for the get_ticket function
def bevestig_keuze_stoel(value_stoel):
    global var_stoel
    var_stoel = value_stoel


# function gets the ticket price and print
def get_ticket():
    print("Gekozen tribune",var_tribune)
    print("Gekozen rij",var_rij)
    print("Gekozen stoel",var_stoel)

    # checks if options are actually chosen else raise error
    try:
        if var_tribune == "" or var_rij == 0 or var_stoel == 0:
            raise ValueError
        else:
            # gets the chosen ticketID and the ticketprice from the database
            print(var_tribune, var_rij, var_stoel)
            query = "SELECT plaatsID,prijsTicket,reserved FROM stadion WHERE tribune =%s and rij=%s and stoel=%s"
            mycursor.execute(query, (var_tribune, var_rij, var_stoel))
            myresult = mycursor.fetchall()
            for x in myresult:
                # second check if chair is free
                if x[2] != "Nee":
                    final = "Deze stoel is niet vrij"
                    answer.config(text=final)
                else:
                    #gets the price from the db
                    prijs = (x[1])
                    final = f"Ticketnr: {var_tribune}{var_rij}{var_stoel}   Prijs: {prijs} euro."
                    answer.config(text=final)
                    # popup messagebox are you sure
                    text_MsgBox = "Ticket "+var_tribune+str(var_rij)+str(var_stoel)+" bestellen"
                    MsgBox = messagebox.askquestion(text_MsgBox, "Bent u zeker ?")
                    if MsgBox == 'yes':
                        # checks if a member is logged-in...if not raises an error (protects databank)
                        if naam == "":
                            messagebox.showerror(title="Fout", message="Er is geen lid aangemeld.")
                        else:
                            # sends the ticketorder to the table stadion
                            query = "UPDATE stadion SET reserved = 'Ja' WHERE tribune =%s and rij=%s and stoel=%s"
                            mycursor.execute(query, (var_tribune, var_rij, var_stoel))
                            # Inserts the Plaats_ID x[1] and lidNumber_ID. in the tabel  reservatie
                            print("Lidnummer en ticketid: ", lidNummer, x[0])
                            query = "INSERT INTO reservatie (lidNummer, plaatsID) VALUES (%s,%s)"
                            val = [lidNummer, x[0]]
                            mycursor.execute(query, val)
                            print("Ticket: ",var_tribune, var_rij, var_stoel," is besteld")
                            db.commit()


    # messagebox foutmelding
    except ValueError:
        messagebox.showerror(title="Fout", message="Geef de juiste gegevens in aub")


# configuration ticketorderbox
ticket = Tk()
ticket.title("FC Syntra Genk")
ticket.state("zoomed")
ticket.config(bg='DodgerBlue3')
ticket.grid_rowconfigure(0, weight=1)
ticket.grid_columnconfigure(0, weight=1)

# print title
header1 = "FC Syntra - Ticket"
L_Title = Label(ticket, text=header1, fg='White', bg='DodgerBlue3', font=('Helvetica', 30))
L_Title.pack(pady=20)

# print member-name
header2 = "Welkom,  "+naam
M_Title = Label(ticket, text=header2, fg='White', bg='DodgerBlue3', font=('Helvetica', 20))
M_Title.pack(pady=1)


#LOGO
my_logo = Image.open("syntrapxl_academie_logo_digitaal_rgb_square.png")
resized = my_logo.resize((200,200), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
new_logo_label = Label(ticket, image=new_logo, bg ="DodgerBlue3")
new_logo_label.place(x=1500, y=70)

## CANVAS ##
# CANVAS: kader voor lijnen
my_canvas = Canvas(ticket, width=1224, height=800, background="DodgerBlue2",highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx= 5, pady = 90)

# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="Red", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="Black", width=8)

# configuration image stadion tribunes
stadion = Image.open("stadion.png")
resized = stadion.resize((450, 280), Image.ANTIALIAS)
new_stadion = ImageTk.PhotoImage(resized)
new_stadion_label = Label(ticket, image=new_stadion, bg="DodgerBlue3")
new_stadion_label.place(relx=0.5, rely=0.36)


bestel = Button(ticket, text="Bestel ticket: ", width="20", font=('Helvetica',9), command=get_ticket)
bestel.place(relx="0.2", rely="0.75")


# Ticketprice frame = answer
frame = Frame(ticket, width=200, height=30, relief="groove", borderwidth=2)
frame.place(relx="0.4", rely="0.745")
answer = Label(frame, text="")
answer.place(relx="0.10", rely="0.10")

exit = Button(ticket, text="Exit ", width="10", font=('Helvetica', 9),command=ticket.destroy)
exit.place(relx="0.90", rely="0.90")


# start program
keuze_tribune()

ticket.mainloop()
