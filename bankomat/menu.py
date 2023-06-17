import mysql.connector
from tkinter import *

import historia
import wplac
import wyplac
import historia
def pokaz_menu(pin):

    okno_menu = Tk()
    okno_menu.geometry('300x300')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="klienci"
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT Saldo FROM klienci WHERE PIN = {pin}")
    myresult = mycursor.fetchall()
    mycursor.execute(f"SELECT ID FROM klienci WHERE PIN = {pin}")
    id = mycursor.fetchall()
    id = id[0][0]
    text = Label(okno_menu,text="saldo "+str(myresult[0][0]))
    text.grid(row=0,column=0)

    def wplata1():
        wplac.wplata(pin)

    def wyplata1():
        wyplac.wyplata(pin)

    def history1():
        historia.history(id)


    WP_button = Button(okno_menu,text = "wplać",command=wplata1)
    WP_button.grid(row=2,column=0)
    WY_button = Button(okno_menu,text = "wyplać",command=wyplata1)
    WY_button.grid(row=3,column=0)
    H_button = Button(okno_menu,text = "historia",command=history1)
    H_button.grid(row=2,column=2)

    okno_menu.mainloop()