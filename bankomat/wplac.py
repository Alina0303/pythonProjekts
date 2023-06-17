import mysql.connector
import datetime
from tkinter import *
def wplata(pin):
    okno_wplata = Tk()
    okno_wplata.geometry('300x300')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="klienci"
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT Saldo FROM klienci WHERE PIN = {pin}")
    saldo = mycursor.fetchall()
    mycursor.execute(f"SELECT ID FROM klienci WHERE PIN = {pin}")
    id_k = mycursor.fetchall()
    data3 = datetime.datetime.now()
    def wykonaj():
        podana_kwota = int(podaj_kwote.get())
        mycursor.execute(f"UPDATE klienci SET Saldo = {saldo[0][0]}+{podana_kwota} WHERE PIN = {pin}")
        mydb.commit()

        mycursor.execute(f"INSERT INTO tranzakcii(ID_T,DATA, Operacja, ID_K) VALUES('','{data3}','wplata {podana_kwota}',{id_k[0][0]})")
        mydb.commit()
        wykonano = Label(okno_wplata,text="wykonano")
        wykonano.grid(row=2,column=0)



    podaj_kwote = Entry(okno_wplata)
    podaj_kwote.grid(row=0,column=0)
    text = Label(okno_wplata,text="kwota")
    text.grid(row=0,column=1)
    wplac_button = Button(okno_wplata,text="wplać",command=wykonaj)
    wplac_button.grid(row=1,column=0)
    okno_wplata.mainloop()