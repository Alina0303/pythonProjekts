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
while True:
	a = int(input('podaj liczbe1:'))
	b = int(input('podaj liczbe2:'))
	c = input('dzalanie:')
	if c == '+':
		print('+'+str(a+b))
	elif c == '-':
		print('-'+str(a-b))
	elif c == '*':
		print('*'+str(a*b))
	elif c == '/':
		print('/'+str(a/b))
	elif c == '%':
		print('%'+str(a%b))
	elif c == '**':
		print('**'+str(a**b))
	d = input()
	if d == 'x':
		break





