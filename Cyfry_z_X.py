
zero = ['  xx  ',
        ' x  x ',
        'x    x',
        'x    x',
        'x    x',
        ' x  x ',
        '  xx  ']

jeden = ['  xx',
         '  xx',
         ' x x',
         'x xx',
         '  xx',
         '  xx',
         '  xx',]

dwa = ['   xx    ',
       ' x    xx ',
       ' x     xx',
       '       xx',
       '     xx  ',
       '   xx    ',
       'xxxxxxxxx']


trzy = ['   xxx  ',
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

szesc = [' xxxx ',
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


dziewiec = [' xxxx ',
            'x    x',
            'x    x',
            '  xxxx',
            '     x',
            'x    x',
            ' xxxx ']


a = input('podaj liczbe :')


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
			tekst_do_wpisania+=szesc[i]
		if a[j]=='7':
			tekst_do_wpisania+=siedem[i]
		if a[j]=='8':
			tekst_do_wpisania+=osiem[i]
		if a[j]=='9':
			tekst_do_wpisania+=dziewiec[i]
		tekst_do_wpisania+='   '
	print(tekst_do_wpisania)
