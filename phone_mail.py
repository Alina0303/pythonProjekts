import requests
from tkinter import *
okno = Tk()
okno.geometry("300x300")

def email():
    url = 'https://fakestoreapi.com/users'

    response = requests.get(url)

    dane = response.json()
    zapiszDoPliku = open(r"C:\Users\user\PycharmProjects\pythonProject\venv\e_mail.txt", 'w')
    for element in dane:
        zapiszDoPliku.write(str(element['email'])+"\n")
    zapiszDoPliku.close()


def telefon():
    url = 'https://fakestoreapi.com/users'

    response = requests.get(url)

    dane = response.json()
    zapiszDoPliku1 = open(r"C:\Users\user\PycharmProjects\pythonProject\venv\telefon.txt", 'w')
    for element in dane:
        zapiszDoPliku1.write(str(element['phone'])+"\n")
    zapiszDoPliku1.close()


mail = Button(text="e-mail",command=email)
mail.grid(row=0,column=0)

phone = Button(text="telefon",command=telefon)
phone.grid(row=1,column=0)
okno.mainloop()
