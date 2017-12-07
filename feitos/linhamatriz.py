#!/usr/bin/python3
#linhamatriz.py 1181

Lc, Cc = 12, 12

L = int(input())
T = input()

matriz = list()

for i in range(Lc):
	matriz.append([0] * Cc)

S, M = 0, 1

for l in range(Lc):
	for c in range(Cc):
		dado = float(input())
		matriz[l][c] = dado

if T == 'S':
	for c in range(3):
		print(matriz[L][c])
		S += matriz[L][c]
	print("{0:.1f}".format(S))

elif T == 'M':
	for c in range(3):
		M *= matriz[L][c]
	print("{0:.1f}".format(M))
