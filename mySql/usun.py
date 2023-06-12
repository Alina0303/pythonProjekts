import mysql.connector
from tkinter import *
def delete():
    okno_delete = Tk()
    okno_delete.geometry("300x300")
    def usun():
        podane_id = id.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="users"
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT id FROM users WHERE 1")
        myresult = mycursor.fetchall()

        for i in myresult:
            if i[0] == podane_id:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="users"
                )
                mycursor = mydb.cursor()
                sql = f"DELETE FROM users WHERE id = '{podane_id}'"
                mycursor.execute(sql)
                mydb.commit()
                result.config(text="usuneto")
            else:
                result.config(text="nie znaleziono")



    etykieta = Label(okno_delete, text="id")
    etykieta.grid(row=1, column=0)
    id = Entry(okno_delete)
    id.grid(row=1, column=1)
    napis = Label(okno_delete,text="usuwanie")
    napis.grid(row=0,column=0)
    usun_button = Button(okno_delete, text="usun", command=usun)
    usun_button.grid(row=2, column=0)
    result = Label(okno_delete, text="")
    result.grid(row=3, column=0)
    okno_delete.mainloop()
