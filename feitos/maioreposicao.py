#!/usr/bin/python3
#maioreposicao 1080

P = 0
M = 0

for i in range(1, 101):
	N = int(input())
	if(N > M):
		M, P = N, i

print("{0}\n{1}".format(M, P))