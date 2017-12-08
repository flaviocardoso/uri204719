#!/usr/bin/python3
#rodizio.py 2712 OK
import re

def dia(s):
	n = int(s[-1])
	retorna = ""
	if n == 1 or n == 2:
		retorna = "MONDAY"
	elif n == 3 or n == 4:
		retorna = "TUESDAY"
	elif n == 5 or n == 6:
		retorna = "WEDNESDAY"
	elif n == 7 or  n == 8:
		retorna = "THURSDAY"
	elif n == 9 or n == 0:
		retorna = "FRIDAY"
	return retorna

N = int(input())

for i in range(N):
	e = input()
	t = re.match(r'[A-Z][A-Z][A-Z]-[0-9][0-9][0-9][0-9]', e)
	if t:
		print(dia(e))
	else:
		print("FAILURE")
print()



'''
TESTE OK 
n = input()

print(dia(n))
/opt/sublime_text/sublime_text %F
'''