#!/usr/bin/python3
#seqofseq.py 2028

from sys import stdin

d = stdin.readline()
c = 0

while d != '':
	c = c + 1
	n = int(d)
	l = list()
	for i in range(n + 1):
		l.append(i)
		if (i > 1):
			for j in range(i - 1):
				l.append(i)
		
	t = len(l)

	if (t > 1):
		print("Caso {0}: {1} numeros".format(c, len(l)))
	else:
		print("Caso {0}: {1} numero".format(c, len(l)))

	for i in range(t):
		print(l[i], end=" ")
	
	print("\n")
	
	d = stdin.readline()