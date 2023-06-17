import mysql.connector
import datetime
from tkinter import *
def wyplata(pin):
    okno_wyplata = Tk()
    okno_wyplata.geometry('300x300')
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
        if podana_kwota<=saldo[0][0]:
            mycursor.execute(f"UPDATE klienci SET Saldo = {saldo[0][0]}-{podana_kwota} WHERE PIN = {pin}")
            mydb.commit()
            mycursor.execute(f"INSERT INTO tranzakcii(ID_T,DATA, Operacja, ID_K) VALUES('','{data3}','wyplata {podana_kwota}',{id_k[0][0]})")
            mydb.commit()
            wykonano = Label(okno_wyplata, text="wykonano")
            wykonano.grid(row=2, column=0)
        else:
            bled = Label(okno_wyplata,text="nie starczy na to")
            bled.grid(row=3,column=0)

    podaj_kwote = Entry(okno_wyplata)
    podaj_kwote.grid(row=0, column=0)
    text = Label(okno_wyplata, text="kwota")
    text.grid(row=0, column=1)
    wyplac_button = Button(okno_wyplata, text="wyplać", command=wykonaj)
    wyplac_button.grid(row=1, column=0)
    okno_wyplata.mainloop()