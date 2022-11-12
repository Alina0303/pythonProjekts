#zmienna_int = 123 #zmienna cialkowita
#zmienna_float = 123.0 #zmienna przeczinkowa
#zmienna_str = 'tekst' #zmienna textowa
#zmienna_str2 = 'tekst2'
#
#
#print(zmienna_str+str(zmienna_int))

#kolekcja = [123,300,400,500]

#print(kolekcja_int[0]+kolekcja_int[1])

#kolekcja_str = ['123','300','400','12gfhd']


#print(float(zmienna_int))
#print(zmienna_float)
#
#print('----wyniki----')
#
#print(zmienna_int/2)
#print(zmienna_float/2)


#slownik = {'pierwszy':'123','drugi':'300','trzeci':200}
#
#print(slownik['pierwszy'])
#
#slownik_zaawansowany = {'aaa':111,'kolekcja':[10,20,30,40,50],'slownik':{'ttt'}}
#print(slownik_zaawansowany['kolekcja'][2])

#a = 10
#b = 20
#c = 30
#if a==b:
#	print('a=b')
#	if b==c:
#		print('a=b=c')
#else:
#	print('falsh')
#
#if a==b and b==c:
#	print('a=b=c')
#else:
#	print('falsz')
#a=1
#while a<=10:
#	print(a)
#	a+=1
#
#a = input('Wpisz swoje imie:')
#b = input('Wpisz lakas lizcbe')
#print('Witaj'+a)
#print('Twoja liczba to: '+ b)
#print(type(b))
#print('twoja liczba dodana do 10 to'+str(int(b)+10))


#while True:
#	print('jestem w programe')
#	a = input()
#	if a == 'x':
#		break
#	else:
#		continue
#	print('dzienki')
#while True:
#	a = int(input('podaj liczbe1:'))
#	b = int(input('podaj liczbe2:'))
#	c = input('dzalanie:')
#
#	if c == '+':
#		print('+'+str(a+b))
#	elif c == '-':
#		print('-'+str(a-b))
#	elif c == '*':
#		print('*'+str(a*b))
#	elif c == '/':
#
#		try:
#			print('/'+str(a/b))
#		except:
#			print('nie mozna dielicz na 0')
#			continue
#
#	elif c == '%':
#		print('%'+str(a%b))
#	elif c == '**':
#		print('**'+str(a**b))
#	d = input('wprowadz x dla zakonczenia programy:')
#	if d == 'x':
#		break

#while True:
#	
#	a = input('podaj liczbe')
#	try:
#		print(float(a)/2)
#	except ValueError as e:
#		print('e')

#from math import randome
#import math
#
#x = float(input(''))
#print(math.log10(x))

import random

#print(randome.randint(0,10))
#
#a = int(input('zgadnij liczbe od 1 do 10'))
#b = random.randint(0,10)
#while a!=b:
#	input('try again')
#print('udalo sie')
#def potegowanie(a,b):
#	return a**b
#	print('a')
#	print('a+10')
#a = potegowanie(2,10)
#print(a)


#def rekurencyjna(a):
#	print(a)
#	a-=1
#	if a<0:
#		rekurencyjna(a)



#def czy_zgadles(a):
#	
#	if a==randint(0.10):
#		return True
#	else:
#		return False
#
#x = False
#while x==False:
#	a=input()
#	x=czy_zgadles(a)

#a = int(input('zgadnij liczbe od 1 do 10'))
#while a!=random.randint(0,10):
#	input('try again')
#print('udalo sie')
#
#def czy_gadlesz(a):
#	if a==randint(0,10):
#		return True
#
#
#
#
#tablica = 'zwykly, tekst'
#
#print(tablica[0])
#print(tablica.split(',')[0])
#print(tablica[:-1])
#print(tablica.replace(',,',','))
#
#
#
#kolekcja=['a','b','c','d']
#for i in range(len(kolekcja)):
#	if i == 2:
#		kolekcja[i]='tekst'
#print(i)



zero=['  xx  ',
      ' x  x ',
      'x    x',
      'x    x',
      'x    x',
      ' x  x ',
      '  xx  ']

jeden=['  xx',
       '  xx',
       ' x x',
       'x xx',
       '  xx',
       '  xx',
       '  xx',]

dwa=['   xx    ',
     ' x    xx ',
     ' x     xx',
     '       xx',
     '     xx  ',
     '   xx    ',
     'xxxxxxxxx']


trzy=['   xxx  ',
      ' xx   xx',
      'x      x',
      '     xx ',
      '      xx',
      'xx    xx',
      '  xxxx  ']

cztery = ['x    x',
          'x    x',
          'x    x',
          'xxxxxx',
          '     x',
          '     x',
          '     x']

piec = ['xxxxxx',
        'x     ',
        'x     ',
        'xxxx  ',
        '     x',
        '     x',
        'xxxxx ']

szeszc = [' xxxx ',
          'x     ',
          'x     ',
          'xxxx  ',
          'x    x',
          'x    x',
          'xxxxx ']

siedem = ['xxxxxxxx',
          '      x ',
          '     x  ',
          '    x   ',
          '   x    ',
          '  x     ',
          ' x      ']

osiem = ['   xxx   ',
         '  x   x  ',
         ' x     x ',
         '   xxx   ',
         ' xx   xx ',
         'x       x',
         '   xxx   ']


dziwienc = [' xxxx ',
            'x    x',
            'x    x',
            '  xxxx',
            '     x',
            'x    x',
            ' xxxx ']


a = input('podaj liczbe :')

#for i in range()
#for i in zero:
#	print(i)



for i in range(7):
	tekst_do_wpisania=''
	for j in range(len(a)):
		if a[j]=='0':
			tekst_do_wpisania+=zero[i]
		if a[j]=='1':
			tekst_do_wpisania+=jeden[i]
		if a[j]=='2':
			tekst_do_wpisania+=dwa[i]
		if a[j]=='3':
			tekst_do_wpisania+=trzy[i]
		if a[j]=='4':
			tekst_do_wpisania+=cztery[i]
		if a[j]=='5':
			tekst_do_wpisania+=piec[i]
		if a[j]=='6':
			tekst_do_wpisania+=szeszc[i]
		if a[j]=='7':
			tekst_do_wpisania+=siedem[i]
		if a[j]=='8':
			tekst_do_wpisania+=osiem[i]
		if a[j]=='9':
			tekst_do_wpisania+=dziwienc[i]
		tekst_do_wpisania+='   '
	print(tekst_do_wpisania)