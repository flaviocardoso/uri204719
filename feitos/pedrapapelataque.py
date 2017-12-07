#!/usr/bin/python3
#pedrapapelataque.py 2031

def jog1():
	print("Jogador 1 venceu")
def jog2():
	print("Jogador 2 venceu")

def jogo(j1, j2):
	if(j1 == "ataque" and j2 == "pedra"):
		jog1()
	if(j1 == "pedra" and j2 == "ataque"):
		jog2()
	if(j1 == "pedra" and j2 == "papel"):
		jog1()
	if(j1 == "papel" and j2 == "pedra"):
		jog2()
	if(j1 == "ataque" and j2 == "papel"):
		jog1()
	if(j1 == "papel" and j2 == "ataque"):
		jog2()
	if(j1 == "papel" and j2 == "papel"):
		print("Ambos venceram")
	if(j1 == "pedra" and j2 == "pedra"):
		print("Sem ganhador")
	if(j1 == "ataque" and j2 == "ataque"):
		print("Anaquilacao mutua")

def jogo2(j1, j2):
	if(j1 == "ataque" or j2 == "ataque"):
		if(j1 == "ataque" and j2 == "ataque"):
			print("Anaquilacao mutua")
		elif(j1 == "ataque"):
			jog1()
		else:
			jog2()
	elif(j1 == "pedra" or j2 == "pedra"):
		if(j1 == "pedra" and j2 == "pedra"):
			print("Sem ganhador")
		elif(j1 == "pedra"):
			jog1()
		else:
			jog2()
	elif(j1 == "papel" or j2 == "papel"):
		if(j1 == "papel" and j2 == "papel"):
			print("Ambos venceram")
		elif(j1 == "papel"):
			jog1()
		else:
			jog2()


n = int(input())

for i in range(n):
	j1 = input().strip()
	j2 = input().strip()

	jogo2(j1, j2)