import mysql.connector

from tkinter import *
def add():
    okno_wprowadz = Tk()
    okno_wprowadz.geometry("300x300")
    def dodaj():
        podany_login = login.get()
        podane_haslo = haslo.get()
        podany_e_mail = e_mail.get()
        podany_typ = int(typ.get())

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="users"
        )
        mycursor = mydb.cursor()

        sql = f"INSERT INTO users (id,login,password,e_mail,typ) VALUES ('','{podany_login}', '{podane_haslo}', '{podany_e_mail}', '{podany_typ}')"


        mycursor.execute(sql)

        mydb.commit()







    napis = Label(okno_wprowadz, text="wprowadzenie")
    napis.grid(row=0, column=0)
    etykieta = Label(okno_wprowadz,text="login")
    etykieta.grid(row=1,column=0)
    login = Entry(okno_wprowadz)
    login.grid(row=1,column=1)
    etykieta1 = Label(okno_wprowadz, text="haslo")
    etykieta1.grid(row=2, column=0)
    haslo = Entry(okno_wprowadz)
    haslo.grid(row=2,column=1)
    etykieta2 = Label(okno_wprowadz, text="e-mail")
    etykieta2.grid(row=3, column=0)
    e_mail = Entry(okno_wprowadz)
    e_mail.grid(row=3,column=1)
    etykieta3 = Label(okno_wprowadz, text="typ")
    etykieta3.grid(row=4, column=0)
    typ = Entry(okno_wprowadz)
    typ.grid(row=4,column=1)
    wprowadz_button = Button(okno_wprowadz,text="dodaj",command=dodaj)
    wprowadz_button.grid(row=5,column=0)
    okno_wprowadz.mainloop()