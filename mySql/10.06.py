import mysql.connector
from tkinter import *
import menu
window = Tk()
window.geometry('300x300')

def zaloguj():
    podany_login = login.get()
    podane_haslo = haslo.get()
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = podany_login,
            password = podane_haslo,
            database = "users"
        )

        menu.pokaz_menu()

    except:
        komunikat.config(text="Blad logowania")


login = Entry()
login.grid(row=0,column=0)

login_napis = Label(text="podaj login")
login_napis.grid(row=0,column=1)

haslo=Entry()
haslo.grid(row=1,column=0)
haslo_napis=Label(text="podaj haslo")
haslo_napis.grid(row=1,column=1)
przycisk_zaloguj = Button(text="zaloguj",command=zaloguj)
przycisk_zaloguj.grid(row=2,column=0)
komunikat = Label(text="")
komunikat.grid(row=3,column=0)
window.mainloop()