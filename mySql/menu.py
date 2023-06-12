import mysql.connector
from tkinter import *
import wyszukaj
import wprowadz
import usun

def pokaz_menu():
    okno_menu = Tk()
    okno_menu.geometry("300x300")
    napis = Label(okno_menu,text="Menu")
    napis.grid(row=0,column=0)

    wprowadz_button = Button(okno_menu,text="Wprowadz",command=wprowadz.add)
    wprowadz_button.grid(row=1,column=0)
    wyszukaj_button = Button(okno_menu,text="wysukaj",command=wyszukaj.serch)
    wyszukaj_button.grid(row=2,column=0)
    usun_button = Button(okno_menu,text = "usun",command=usun.delete)
    usun_button.grid(row=3,column=0)
    okno_menu.mainloop()