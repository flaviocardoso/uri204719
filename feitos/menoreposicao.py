#!/usr/bin/python3
#menoreposicao.py 1180

N = int(input())
lista = list(map(int, input().split()))
P, M = 0, lista[0]

for i in range(1, N):
	if(lista[i] < M):
		P, M = i, lista[i]
print("Menor valor: {0}\nPosicao: {1}".format(M, P))