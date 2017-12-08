#!/usr/bin/python3
#sequenciaij3 1097

a, b = 7, 4

for i in range(1, 10, 2):
	for j in range(a, b, -1):
		print("I={0} J={1}".format(i, j))
	a, b = a + 2, b + 2