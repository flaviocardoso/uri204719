#!/usr/bin/python3
#maiorrepeticaonumero.py

from collections import Counter
import timeit

def maiorfrequencia():
	ent = [2, 3, 4, 5, 7, 6, 5, 3, 9, 6, 0, 2, 3, 4, 8, 4, 5, 2, 3, 0, 3, 4]#list(map(int, input().split()))
	rep = Counter(ent)
	rep = [[v, k] for k, v in rep.items()]
	rep.sort()
	rep.reverse()
	print(rep[0][1])

mf1 = timeit.Timer('maiorfrequencia()', 'from __main__ import maiorfrequencia')

print(mf1.repeat(4 , 1))

"""

ent = list(map(int, input().split()))

rep = Counter(ent)

print(rep)

rep = [[v, k] for k, v in rep.items()]

print(rep)

rep.sort()
rep.reverse()

print(rep[0][1])

"""