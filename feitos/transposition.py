#!/usr/bin/python3
#transposition.py

palava = "hlowrdelol"

tam = len(palava)
c = 0
for i in range(tam):
	if (i%5) % 2 == 0:
		c = c + 1

crip1 = palava[0:c]
crip2 = palava[c: tam]

pw = ""
for i in range(len(crip1)):
	a = i + 1
	if a%3 != 0:
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

print(decrip)