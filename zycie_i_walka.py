import random

class Czlowiek:
    zycie = 100
    exp = 0
    obrazenia = 0

    def __init__ (self,imie):
        self.imie = imie

    def informacie(self):
        print('imie:'+self.imie)
        print('exp:'+str(self.exp))
        print('zycie:'+str(self.zycie))

    def walka(self):
        self.obrazenia = random.randint(1,100)
        print('Odnosisz obrazenia:'+str(self.obrazenia))
        self.zycie -= self.obrazenia
        if self.zycie<=0:
            print('nie przezyles')
        else:
            self.exp+=100
    def leczenie(self):
        self.zycie = 100


print('Witam w gre')
czlowiek = Czlowiek(input('Imie:'))


print('w - walka')
print('l - lieczenie')
print('s - statystyki')
print('x - wyjscie z gry')
while(True):
    a = input('Twoje dzalanie:')
    if a == 'w':
        czlowiek.walka()
    if a == 'l':
        czlowiek.leczenie()
    if a == 's':
        czlowiek.informacie()
    if a == 'x':
        break
    if czlowiek.exp==1000:
        print('Twyj exp to 1000.Wygrales!')
        break
    if czlowiek.zycie<=0:
        break
