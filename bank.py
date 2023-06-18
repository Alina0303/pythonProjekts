class Person:
    konto = 0
    def __init__(self,imie):
        self.imie = imie
    def pokaz(self):
        print(self.imie)

class BankCustomer:
    def __init__(self,klient):
        self.klient = klient

    def pokaz_imie(self):
        print(self.klient.imie)

    def deposit(self,add):
        self.klient.konto += add
        print(self.klient.imie,self.klient.konto)

    def withdraw(self,odejmij):
        if odejmij <= self.klient.konto:
            self.klient.konto -= odejmij
            print(self.klient.imie,self.klient.konto)
        else:
            print('za mały stan konta')
    def transfer(self, resiwer, kwota):
        if kwota <= self.klient.konto:
            self.withdraw(kwota)
            resiwer.deposit(kwota)
        else:
            print('za mały stan konta')

    def addInterest(self,procent):
        self.klient.konto +=(self.klient.konto/100)*procent
        print(self.klient.imie,self.klient.konto)

osoba1 = Person("ala")
osoba2 = Person("jan")
ala = BankCustomer(osoba1)
ala.pokaz_imie()
jan = BankCustomer(osoba2)
jan.pokaz_imie()
jan.deposit(1000)
ala.deposit(2000)
ala.withdraw(500)
jan.addInterest(4.5)



jan.transfer(ala,500)

