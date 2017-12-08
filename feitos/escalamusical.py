#escala musical
"""
do re mi fa sol la si

vetor = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

vetor_num = [2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1]

Entrada
A primeira linha da entrada terá um número inteiro N, com 1 ≤ N ≤ 105 ,
correspondente ao número de notas musicais da música. 
Em seguida, serão fornecidos N números, um por linha,
todos entre 1 e 61, inclusive, correspondendo às notas musicais.

Seu programa deve verificar se a música está em algum tom maior. 
Em caso afirmativo, seu programa deve imprimir uma única linha com o 
tom maior (sem acentos) em que a música está. Caso contrário, 
seu programa deve imprimir uma linha contendo a palavra desafinado. 
Caso a música possa estar em mais de um tom maior imprima aquele 
relativo a menor nota musical básica, sendo que “do” < “do#” < “re”, . . .

"""

vetor = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
vetor_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

"""
si = [si, do#, re#, mi, fa#, sol#, la#]
la# = [la#, do, re, re#, fa, sol, la]
la = [la, si, do#, re, mi, fa#, sol#]
sol# = [sol#, la#, do, do#, re#, fa, sol] 
sol = [sol, la, si, do, re, mi, fa#]
fa# = [fa#, sol#, la#, si, do#, re#, fa]
fa = [fa, sol, la, la#, do, re, mi]
mi = [mi, fa#, sol#, la, si, do#, re#]
re# = [re#, fa, sol, sol#, la#, do, re]
re = [re, mi, fa#, sol, la, si, do#]
do# = [do#, re#, fa, fa#, sol#, la#, do]
do = [do, re, mi, fa, sol, la, si]
"""

vetor_intervalo = [2, 2, 1, 2, 2, 2, 1]

N = int(input())
Nmenor = 12


c = 0
saida = ""
'''
for i in range(N):
	print(vetor[e%12 - 1])
	e = e + vetor_intervalo[i%len(vetor_intervalo)]
'''
vetor_ent = list()

for i in range(N):
	e = (int(input()) - 1)%12
	if(e < Nmenor):
		Nmenor = e
	vetor_ent.append(e)
	#print(vetor[e%12 - 1])
	#e = e + vetor_intervalo[i%len(vetor_intervalo)]
#for i in range(N):
print("vetor e normal:", vetor_ent)
vetor_ent.sort()
print("vetor e ordenado", vetor_ent)
vetor_ent = sorted(list(set(vetor_ent)))
print("vetor e sem repetição: ", vetor_ent)

for i in vetor_ent:
	#arrumar vetor para ficar em intonação com a nota
	print("nota", vetor[i])
h = 0
t = 0
a = 0
b = 0
c = -1

th = len(vetor_ent) - 1
men = ""
for a in range(th):
	c = 0
	sv = 0
	for b in range(th):
		#if(vetor_ent[b + 1] == vetor_index[vetor_ent[b + a] + vetor_intervalo[b + a]]):
			#c = c + 1
			#t = vetor_ent[a]
		print()	#sv = sv + vetor_intervalo[b]
		print("vetor s", vetor_ent[b + 1])
		print("vetor r", (vetor_ent[(b + a)%th] + vetor_intervalo[b%7]))
		
		if(vetor_ent[b + 1] == (vetor_ent[(b + a)%th] + vetor_intervalo[b%7])):
			print("nota loop:", vetor[vetor_ent[a]])
			c = c + 1
			print("th", th, ", c", c)
		if(c == 4): break
		b = b + 1
		print("contado b", b)
	if(c == 4): break
	a = a + 1
	print("contado a", a)
print(vetor[Nmenor], vetor[t])