import mysql.connector
from tkinter import *
import menu
okno = Tk()
okno.geometry("300x300")
podaj_pin = Entry()
podaj_pin.grid(row=0,column=0)
pin = podaj_pin.get()
def zaloguj():
    global pin
    pin = int(podaj_pin.get())

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="klienci"
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM klienci Where PIN = {pin}")
    myresult = mycursor.fetchall()


    if len(myresult) == 0:
        komunikat.config(text="Blad logowania")

    else:
        menu.pokaz_menu(pin)






text = Label(text="Podaj PIN")
text.grid(row=0,column=1)
zalog_button = Button(text = "Zaloguj",command=zaloguj)
zalog_button.grid(row=1,column=0)
komunikat = Label(text="")
komunikat.grid(row=2,column=0)

okno.mainloop()