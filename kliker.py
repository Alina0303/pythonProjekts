from tkinter import *
okno = Tk()

okno.geometry("500x500")
c = Canvas(width=2500,height=2500,bg="purple1")
c.focus_set()
c.pack()

y = 0.25
score = 0
cenaKlika=1
def kliker():
    rakieta = PhotoImage(file=r"rakieta1.png")
    global cenaKlika
    global score
    score += cenaKlika
    result.config(text=score)

    if score >= 10000:
        move()

def sklepik():
    sklep =Tk()
    sklep.geometry("200x200")
    def klik_10():
        global score
        global cenaKlika
        if score >=10:
            score -= 10
            cenaKlika = 10
            sklep.destroy()
            result.config(text=score)
            rakieta.config(file=r"rakieta2.png")
        else:
            etykieta = Label(sklep,text="nie starczy na to")
            etykieta.grid(row=3,column=0)

    def klik_100():
        global score
        global cenaKlika
        if score >=100:
            score -= 100
            cenaKlika = 100
            sklep.destroy()
            result.config(text=score)
            rakieta.config(file=r"rakieta3.png")
        else:
            etykieta = Label(sklep,text="nie starczy na to")
            etykieta.grid(row=3,column=0)

    def klik_1000():
        global score
        global cenaKlika
        if score >=1000:
            score -= 1000
            cenaKlika = 1000
            sklep.destroy()
            result.config(text=score)
            rakieta.config(file=r"rakieta4.png")

        else:
            etykieta = Label(sklep,text="nie starczy na to")
            etykieta.grid(row=3,column=0)


    poziom1=Button(sklep,text="klik=10",command=klik_10,bg="yellow")
    poziom1.place(relx=0.4,rely=0.1)
    poziom2=Button(sklep,text="klik=100",command=klik_100,bg="DarkOrange2")
    poziom2.place(relx=0.4,rely=0.3)
    poziom3=Button(sklep,text="klik=1000",command=klik_1000,bg="red")
    poziom3.place(relx=0.4,rely=0.5)



def move():
    global y
    x = 0.25
    y -=0.003
    klik.place(relx=x, rely=y)
    okno.after(100, move)


store = Button(bg="PowderBlue",fg="purple1",text="Sklepik",command=sklepik)
store.place(relx=0,rely=0)

rakieta = PhotoImage(file=r"rakieta1.png")
klik = Button(bg = "purple1",image=rakieta,command=kliker)
klik.place(relx=0.25,rely=0.25)

result = Label(text="",bg="purple1",fg="PowderBlue")
result.place(relx=0.9,rely=0)
okno.mainloop()