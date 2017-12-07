#!/usr/bin/python3
#transposicao.py
#criptação
m = input()
t = len(m)

mens = ""

for i in range(t):
	if m[i] != " ":
		mens += m[i]
tm = len(mens)

print("Mensagem original: " + mens)

crip1 = list()
crip2 = list()

for a in range(tm):
	if (a%5)%2==0:
		crip1.append(mens[a])
	else:
		crip2.append(mens[a])

#print(crip1)
#print(crip2)

crip = ""
for i in range(len(crip1)):
	crip += crip1[i]
for i in range(len(crip2)):
	crip += crip2[i]

print("Mensagem criptografada: " + crip)
'''
decrip1 = list()
decrip2 = list()
tc = len(crip)

t1 = 0
t2 = 0

for a in range(tm):
	if (a%5)%2==0:
		t1 += 1
	else:
		t2 += 1

print(crip[0:t1])
print(crip[t1:tc])
decrip1 = crip[0:t1]
decrip2 = crip[t1:tc]

for i in range(tc):
	

print(decrip1)
print(decrip2)
'''
#decriptação
tam = len(crip)
c = 0
for i in range(tam):
	if (i%5) % 2 == 0:
		c = c + 1

crip1 = crip[0:c]
crip2 = crip[c: tam]

pw = ""
for i in range(len(crip1)):
	a = i + 1
	if a%3 != 0 and i < (len(crip1) - 1):
		pw = pw + crip1[i] + " "
	else:
		pw = pw + crip1[i]

decrip = list(pw)
#print(decrip)
d = 0
for i in range(len(decrip)):
	if decrip[i] == " ":
		decrip[i] = crip2[d]
		d = d + 1

#print(decrip)
palavra = "".join(decrip)

print("Mensagem descriptografada: " + palavra)



'''for i in range(2):
	

decrip = ""
for i in range(len(decrip1)):
	decrip += decrip1[i]
for i in range(len(decrip2)):
	decrip += decrip2[i]

print(decrip)
'''