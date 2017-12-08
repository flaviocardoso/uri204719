#!/bin/python3
#poucafrequencia.py - uri 1277
import re
'''
S = input()

print(re.sub(u'[M]', '', S))
'''

N = int(input())

for x in range(N):
	nnomes = int(input())
	nomes = list(input().split())
	registros = list(input().split())
	back = ""	
	for i in range(len(nomes)):
		reg = re.sub(u'[M]', '', registros[i])
		regt = len(reg)
		regp = len(re.sub(u'[A]', '', reg))
		f = regp / regt
		if(f < 0.75):
			#print(nomes[i])
			back = back + nomes[i]
		back = back + " "
	print(back.strip())


