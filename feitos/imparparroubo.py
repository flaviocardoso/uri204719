#!/usr/bin/python3
#imparparroubo.py 2059

def jog1():
	print("Jogador 1 ganha!")
def jog2():
	print("Jogador 2 ganha!")

def imparparroubo(p, j1, j2, r, a):
	soma = j1 + j2

	if(r == 1):
		if(a == 1):
			jog2()
		else:
			jog1()
	else:
		if(a == 1):
			jog1()
		else:
			if(p == 1):
				if(soma%2==0):
					jog1()
				else:
					jog2()
			else:
				if(soma%2==0):
					jog2()
				else:
					jog1()

p, j1, j2, r, a = map(int, input().split())

imparparroubo(p, j1, j2, r, a)