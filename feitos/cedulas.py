ceds = int(input())

s = 0

if(ceds > 0 and ceds < 1000000):
	print("%d" % ceds)
	s = ceds / 100
	print("%d nota(s) de R$ 100,00" % s)
	ceds = ceds % 100
	s = ceds / 50
	print("%d nota(s) de R$ 50,00" % s)
	ceds = ceds % 50
	s = ceds / 20
	print("%d nota(s) de R$ 20,00" % s)
	ceds = ceds % 20
	s = ceds / 10
	print("%d nota(s) de R$ 10,00" % s)
	ceds = ceds % 10
	s = ceds / 5
	print("%d nota(s) de R$ 5,00" % s)
	ceds = ceds % 5
	s = ceds / 2
	print("%d nota(s) de R$ 2,00" % s)
	ceds = ceds % 2
	s = ceds / 1
	print("%d nota(s) de R$ 1,00" % s)
	ceds = ceds % 1