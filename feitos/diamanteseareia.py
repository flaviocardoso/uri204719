#!/usr/bin/python3
#diamanteseareia.py 1069
import re

N = int(input())
d = 0

for i in range(N):
	e = input()
	s = list()
	for i in e:
		if i == "<" or i == ">":
			s.append(i)

	print(s)

'''
entrada
2
<..><.<..>>
<<<..<......<<<<....>
saida
3
1

'''