#!/usr/bin/python3
#detectorfalhas.py

from sys import stdin
data = stdin.readline()
maior = int(data)
temp = data
while data != '':	
	if maior < int(temp):
		data = temp	
	d = int(data)
	if d >= maior:
		maior = d
	else:
		menor = d
	data = stdin.readline()
	temp = data
	
print(maior + 1)
#não resolvido

'''

while True:

	try:
		data = input()
	except EOFError:
		break	

	print(data)
'''