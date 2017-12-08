#!/usr/bin/python3
#mediaponderada 1079

N = int(input())

for i in range(N):
	lista = list(map(float, input().split()))
	print("{0:.1f}".format((lista[0]*0.2 + lista[1]*0.3 + lista[2]*0.5)))