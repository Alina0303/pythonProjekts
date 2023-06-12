import requests
from tkinter import *
okno = Tk()
okno.geometry("300x300")
def oblicz():
    url ="http://api.nbp.pl/api/exchangerates/tables/a/"
    podana_cena=float(cena.get())
    response = requests.get(url)
    dane = response.json()
    print(dane)
    for element in dane:
        rate = element['rates']
        for x in rate:
            code = x['code']
            if code == "USD":
                usd_cena = Label(text=str(float(podana_cena/(x['mid'])).__round__(2))+" USD")
                usd_cena.grid(row=3,column=0)

            if code == "EUR":
                eur_cena = Label(text = str(float(podana_cena/(x['mid'])).__round__(2))+" EUR")
                eur_cena.grid(row=4,column=0)

            if code == "GBP":
                gbp_cena = Label(text=str(float(podana_cena/(x['mid'])).__round__(2))+" GBP")
                gbp_cena.grid(row=5, column=0)

cena=Entry()
cena.grid(row=0,column=0)
zl = Label(text="zl")
zl.grid(row=0,column=1)
oblicz_bt = Button(text="oblicz",command=oblicz)
oblicz_bt.grid(row=1,column=0)
okno.mainloop()
