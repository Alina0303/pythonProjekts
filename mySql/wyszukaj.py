import mysql.connector
from tkinter import *
def serch():
    okno_wyszukaj = Tk()
    okno_wyszukaj.geometry("300x300")
    def szukaj():
        podany_login = login.get()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="users"
            )
            mycursor = mydb.cursor()
            mycursor.execute(f"SELECT e_mail,typ FROM users WHERE login = '{podany_login}'")
            myresult = mycursor.fetchall()
            result.config(text=f"email:{myresult[0][0]}\n"
                                              f"typ:{myresult[0][1]}")

        except:
            result.config(text="nie znaleziono")






    napis = Label(okno_wyszukaj, text="wyszukiwanie")
    napis.grid(row=0, column=0)
    etykieta = Label(okno_wyszukaj, text="login")
    etykieta.grid(row=1, column=0)
    login = Entry(okno_wyszukaj)
    login.grid(row=1, column=1)
    wyszukai_button = Button(okno_wyszukaj, text="wyszukaj", command=szukaj)
    wyszukai_button.grid(row=2, column=0)
    result = Label(okno_wyszukaj, text="")
    result.grid(row=3, column=0)
    okno_wyszukaj.mainloop()