#!/usr/bin/python3
#colunamatriz.py 1182

Lc, Cc = 12, 12

C = int(input())
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
	for l in range(3):
		S += matriz[l][C]
	print("{0:.1f}".format(S))

elif T == 'M':
	for l in range(3):
		M *= matriz[l][C]
	print("{0:.1f}".format(M))
