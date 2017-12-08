#!/usr/bin/python3
#teste.py - matrizquadrada1.py 1435

n = int(input())

while n != 0:
	matriz = list()
	for i in range(n):
		#coluna = list()
		#for j in range(n):
		#	coluna.append(1)
		matriz.append([1]*n)
    
	#print(matriz)
    
	zi, zf = 1, n - 1

	while zi <= zf:
		for i in range(zi, zf):
			for j in range(zi, zf):
				matriz[i][j] = zi + 1
		zi = zi + 1
		zf = zf - 1

	#print(matriz)
	#print(d)
	
	for i in range(n):
		for j in range(n):
			print(matriz[i][j], end=" ")
		print()
	print()
	n = int(input())