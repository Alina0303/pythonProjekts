import mysql.connector
from tkinter import *
def history(id):
    okno_historia = Tk()
    okno_historia.geometry('300x300')
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="klienci"
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM tranzakcii WHERE ID_K = '{id}'")
    myresult = mycursor.fetchall()

    x = 0
    for i in myresult:
        hist = Label(okno_historia,text=i)
        hist.grid(row=x,column=0)
        x += 1


    okno_historia.mainloop()


