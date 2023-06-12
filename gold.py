import requests
from tkinter import *
okno = Tk()
okno.geometry("300x300")
def pokaz():
    podane_dni = dni.get()
    url = 'http://api.nbp.pl/api/cenyzlota/last/'+podane_dni

    response = requests.get(url)

    dane = response.json()
    print(dane)
    ceny = []
    for element in dane:
        ceny.append(element['cena'])
    print(ceny)
    for i in ceny:
        if i<=ceny[0]:
            minimalna = i
        if i>=ceny[0]:
            maksymalna = i
    for element in dane:
        if element['cena']==minimalna:
            mini = Label(text=str(element['data'])+" "+str(minimalna)+" minimalna cena")
            mini.grid(row=2,column=0)

        if element['cena']==maksymalna:
            maks = Label(text=str(element['data'])+" "+str(maksymalna)+" maksymalna cena")
            maks.grid(row=3,column=0)
dni = Entry()
dni.grid(row=0, column=0)
ile = Label(text="ile dni")
ile.grid(row=0, column=1)
pokaz_bt = Button(text="pokaz", command=pokaz)
pokaz_bt.grid(row=1, column=0)
okno.mainloop()
