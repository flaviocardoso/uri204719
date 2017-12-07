#!/usr/bin/python3
#buble.py

vetor = list(map(int, input().split()))

# algoritmo - comp(vetor)
print(vetor)
t = len(vetor) - 1
aux = 0
#conferte vetor
def min(v, a, b):
	aux = v[a]
	v[a] = v[b]
	v[b] = aux
#min(vetor, 0, 1)

for i in range(t, 0, -1):
	for j in range(0, i):
		if vetor[j] > vetor[j+1]:
			min(vetor, j, j+1)
print(vetor)