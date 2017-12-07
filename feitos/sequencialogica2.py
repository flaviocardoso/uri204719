#!/usr/bin/python3
#sequencialogica2.py 1145

C, N = map(int, input().split())

for i in range(1, N + 1, C):
	for j in range(i, C + i):
		print(j, end=" ")
	print()