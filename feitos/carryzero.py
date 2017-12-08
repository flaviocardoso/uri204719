
'''
4  = 00000000 00000000 00000000 00000100
+6 = 00000000 00000000 00000000 00000110
----------------------------------------
2  = 00000000 00000000 00000000 00000010

#4 6   -- saida 2
#6 9   -- saida 15
'''

"""
def inttobit(e):
	s = ""
	while(e >= 0):
		s = s + str(e%2)
		e = e - e/2
	return s

"""

def carryzero(s):
	v = s.split()

	n1 = int(v[0])
	n2 = int(v[1])

	b1 = "{0:b}".format(n1)
	b2 = "{0:b}".format(n2)

	cb1 = len(b1)
	cb2 = len(b2)

	if(cb1 >= cb2):
		if(cb1 == cb2):
			bm = cb1
		else:
			bm = len(b1)
			r = len(b1) - len(b2)
			b2 = ('0' * r) + b2 
	else:
		bm = len(b2)
		r = len(b2) - len(b1)
		b1 = ('0' * r) + b1

	b = ""
	for i in range(bm):
		if(b1[i] == b2[i]):
			b = b + '0'
		else:
			b = b + '1'

	return "%d" % int(b, 2)

try:
	#s = input()
	v = []
	while ((s = input()) != ""):
		v.append(carryzero(s))	
		#s = input()

	for x in v:
		print(x)
except EOFError as e:
	raise e

