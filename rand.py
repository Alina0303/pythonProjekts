def Czy_zgadles(a):

	if a == random.randint(0,10):
		return True
	else:
		return False

x = False
while x == False:
	try:
		a = int(input('zgadnij liczbe od 1 do 10:'))
	except:
		print('Mozesz podacz tylko liczby cialkowite!')
		continue
	x = Czy_zgadles(a)
print('udalo sie')
