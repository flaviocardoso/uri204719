#!/usr/bin/python3
#sequencialogica.py 1144

N = int(input())

for i in range(1, N + 1):
	for j in range(2):
		e = pow(i, 2)
		em = e * i
		print("{0} {1} {2}".format(i, e + j, em + j))