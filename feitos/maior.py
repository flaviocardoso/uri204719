ent = input()

v = ent.split()

a = int(v[0])
b = int(v[1])
c = int(v[2])

if(a > b):
	if(a > c):
		m = a
	else:
		m = c
else:
	if(b > c):
		m = b
	else:
		m = c

print("%d eh o maior" % m)		